class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0

        for i in range(len(prices)):
            j=i+1  
            while j< len(prices):
                if(prices[j]-prices[i]> profit):
                    profit=prices[j]-prices[i]
                j+=1
        return profit

    
        