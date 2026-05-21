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

        
        

        