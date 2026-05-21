class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        sum=0
        for i in range(len(nums)):
            if nums[i]+sum>=nums[i]:
                sum+=nums[i]
                nums[i]=sum
            else:
                sum=nums[i]
        return max(nums)




       

        