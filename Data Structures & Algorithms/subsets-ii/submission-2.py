class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, sol=[],[]
        def dfs(i):
            if sorted(sol) not in res:
                res.append(sorted(sol).copy())
            if i==len(nums):
                return
            sol.append(nums[i])
            dfs(i+1)
            sol.pop()
            dfs(i+1)
        dfs(0)
        return res