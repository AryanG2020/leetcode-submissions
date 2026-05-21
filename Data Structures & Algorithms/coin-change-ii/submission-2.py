class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo={}
        def dfs(amount, i):
            if amount==0:
                return 1
            if amount<0 or i>=len(coins):
                return 0
            if (amount, i) in memo:
                return memo[(amount, i)]
            memo[(amount,i)]= dfs(amount-coins[i], i)+dfs(amount,i+1)
            return memo[(amount,i)]
        res=dfs(amount,0)
        return res

# That line is the absolute heart of the algorithm! It handles both the decision-making (how we build combinations) and the memory (how we avoid doing the exact same work twice).

# Let's break it down into two parts: the right side (the decisions) and the left side (the memo).

# 1. The Right Side: The Two Decisions
# dfs(amount - coins[i], i) + dfs(amount, i + 1)

# In this problem, you have an infinite supply of coins. At any given moment, you are looking at a specific coin (at index i) and you have to make a choice. This line adds the results of the two possible choices together to get the total number of valid combinations:

# Choice A: "Use the coin" -> dfs(amount - coins[i], i)
# You subtract the coin's value from the amount you need to make. Notice that we pass i (not i + 1) into the next recursive call. Because you have an infinite supply, you might want to use this exact same coin again on the next turn.

# Choice B: "Skip the coin" -> dfs(amount, i + 1)
# You decide not to use the current coin. The amount stays exactly the same, but you move your index to i + 1 to start looking at the next coin in the list.

# The + between them means: "The total number of ways to make this amount is the number of ways if I use this coin PLUS the number of ways if I skip it."

# 2. The Left Side: What memo is storing
# memo[(amount, i)] = ...

# The memo (short for memoization) is a Python dictionary acting as a cache.

# It stores the answer to a very specific subproblem. The tuple (amount, i) represents the unique "state" of your current situation. It translates to the question: "How many combinations are there to make this specific amount using only the coins from index i to the end of the list?"

# For example, if you need to make an amount of 5, and your current coin index i is 1, memo[(5, 1)] will store the final integer answer to that exact scenario once it finishes calculating.



        
        

        