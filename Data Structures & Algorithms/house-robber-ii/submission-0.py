class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        def rob_linear(houses):
            prev, curr = 0, 0
            for amount in houses:
                prev, curr = curr, max(curr, prev + amount)
            return curr

    # Case 1: Exclude the last house
        max1 = rob_linear(nums[:-1])
    # Case 2: Exclude the first house
        max2 = rob_linear(nums[1:])

        return max(max1, max2)
        