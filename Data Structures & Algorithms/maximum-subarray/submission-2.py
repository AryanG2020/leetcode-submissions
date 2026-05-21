class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        track=0
        res=[nums[0]]
        for num in nums[1:]:
            if res[-1]>0:
                res.append(res[-1]+num)
            else:
                res.append(num)
        return max(res)

            


      




       

        