class Solution:
    def maxArea(self, heights: List[int]) -> int:
       #brute force
       # maxval=0
       # for i in range(len(heights)):

        #    for j in range(len(heights) ):
         #       if i!=j:
          #          width=abs(i-j)
           #         maxval= max(maxval, width* min(heights[i],heights[j]))
        #return maxval

        maxval=0
        l=0
        r=len(heights)-1

        while l<r:
            width=r-l
            maxval= max(maxval, min(heights[l],heights[r])* width)
            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1
        return maxval
                

