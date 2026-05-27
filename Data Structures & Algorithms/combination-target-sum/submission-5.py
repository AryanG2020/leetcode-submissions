class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, sol=[],[]
        myset=set()
        def dfs(n, total):
            if total>target or n==len(nums):
                return 
            if total==target and tuple(sol) not in myset:
                res.append(sol.copy())
                myset.add(tuple(sol))
            sol.append(nums[n])
            dfs(n, total+nums[n])
            sol.pop()
            dfs(n+1, total)
        dfs(0,0)
        return res
            

        