class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        myset=set()
        for i in range(len(nums)):
            if nums[i] in myset:
                return nums[i]
            else:
                myset.add(nums[i])
        return None
        