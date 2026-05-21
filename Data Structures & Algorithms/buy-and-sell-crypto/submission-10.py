class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest=prices[0]
        profit=0
        for price in prices:
            diff=price - lowest
            if lowest>price:
                lowest=price
            profit=max(diff,profit)
        return profit
        
   
            




        
        