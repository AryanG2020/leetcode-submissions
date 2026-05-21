class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1, max(piles)
        k=max(piles)
        while l<=r:
            m=(l+r)//2
            totalHours=0
            for pile in piles:
                totalHours+=math.ceil(pile/m)
            if totalHours<=h:
                k=min(k, m)
                r=m-1
            elif totalHours>h:
                l=m+1
        return k



        