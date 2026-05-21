class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxval=0
        for i in range(len(heights)):

            for j in range(len(heights) ):
                if i!=j:
                    width=abs(i-j)
                    maxval= max(maxval, width* min(heights[i],heights[j]))
        return maxval
                

