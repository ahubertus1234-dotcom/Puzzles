Let $S$ be the set of length 3 sequences composed of $H$ and $T$. We have 
$$
    S:=\{HHH,\ HHT,\ HTH,\ HTT,\ THH,\ THT,\ TTH,\ TTT\}.
$$
Let player 1 select a sequence from $S$. After seeing player 1's choice, player 2 chooses an alternate sequence from $S$. The players will observe the tosses of a fair coin until a player wins upon the first time his sequence is tossed. 

The following strategy is a "good strategy" for player 2. 

Suppose player 1 chooses $A=abc$.  Player 2 responds with $B=\bar{b}ab$ from $S$, where $\bar{b}$ denotes the "opposite" of $b$. For $A$ to occur, $ab$ must be tossed. 

Consider the toss preceding the occurence of $ab$ and note that it must be $\bar{b}$ or $b$. In the former case, $\bar{b}ab$ has already occurred so that player 2 has won. In the latter case, the game continues on. 

Thus whenever player 1 is in a winning position, player 2 could win on the preceding toss. 

We will computationally verify that this strategy, $\mathbb P(\text{player 2 wins})\ge 2/3$ regardless of player 1's choice. By comparing it with every possible response available to Player 2, we will also show that the described strategy is not merely a good strategy, but rather the optimal strategy. 