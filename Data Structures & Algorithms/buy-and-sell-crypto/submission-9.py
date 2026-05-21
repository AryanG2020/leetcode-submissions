class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        lowest=prices[0]
        for price in prices:
            difference= price- lowest
            profit=max(profit, difference)
            if price<lowest:
                lowest=price
        return profit

        