from fractions import Fraction
from sympy import Matrix


# All possible length-3 patterns
patterns = [
    "HHH", "HHT", "HTH", "HTT",
    "THH", "THT", "TTH", "TTT"
]


def get_prefixes(A, B):
    # Proper prefixes of A and B, including the empty string
    return list(set(["", A[:1], A[:2], B[:1], B[:2]]))


def next_state(state, toss, A, B):
    # Add the new toss to the useful recent history
    s = state + toss

    # Check whether A or B has won
    if s.endswith(A):
        return "A"

    if s.endswith(B):
        return "B"

    prefixes = get_prefixes(A, B)

    # Keep prefixes that match the end of s
    possible = [p for p in prefixes if s.endswith(p)]

    # Keep the longest useful suffix
    return max(possible, key=len)


def win_probability(A, B):
    # The transient states are the proper prefixes
    states = get_prefixes(A, B)

    n = len(states)

    # Build M and b for M p = b
    M = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    b = [Fraction(0) for _ in range(n)]

    # Build one equation for each state
    for i, state in enumerate(states):

        # p_state starts on the left side
        M[i][i] = 1

        # Consider H and T
        for toss in "HT":
            nxt = next_state(state, toss, A, B)

            # If B wins immediately
            if nxt == "B":
                b[i] += Fraction(1, 2)

            # If neither player has won
            elif nxt != "A":
                j = states.index(nxt)

                # Move (1/2) p_next to the left side
                M[i][j] -= Fraction(1, 2)

    # Solve M p = b
    p = Matrix(M).inv() * Matrix(b)

    # Return B's win probability from the starting state ""
    return p[states.index("")]


# For each A, find the best response B
for A in patterns:

    best_B = None
    best_p = -1

    for B in patterns:

        if B == A:
            continue

        p = win_probability(A, B)

        if p > best_p:
            best_p = p
            best_B = B

    print(A, "->", best_B, best_p)