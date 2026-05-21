class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(start, comb):
            if len(comb) == 3:
                if sum(comb) == 0:
                    res.append(comb[:])
                return

            for i in range(start, len(nums)):
                # Skip duplicates
                if i > start and nums[i] == nums[i - 1]:
                    continue
                comb.append(nums[i])
                dfs(i + 1, comb)
                comb.pop()

        dfs(0, [])
        return res