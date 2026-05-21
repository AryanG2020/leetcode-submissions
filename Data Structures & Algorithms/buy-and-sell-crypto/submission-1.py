class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low,high=0,len(prices)-1
        maxP=max(0, prices[high]-prices[low])

        for i in range(len(prices)):
            if prices[i]<prices[low] and i<len(prices)-1:
                low=i
                high=i+1
            if prices[i]>prices[high]:
                high=i       
            maxP=max(maxP,prices[high]-prices[low] )
        return maxP
        
            
    
        