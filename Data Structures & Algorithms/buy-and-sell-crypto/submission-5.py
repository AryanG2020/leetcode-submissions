class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low=prices[0]
        maxP=0

        for price in prices:
            if low>price:
                low=price
            maxP= max(price-low, maxP)
        return maxP
            

        
            
    
        