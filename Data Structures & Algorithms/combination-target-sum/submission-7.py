class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        sol,res=[],[]
        def dfs(i, total):
            if total>target or i==len(nums):
                return
            if total==target:
                sol.append(res.copy())
                return
            res.append(nums[i])
            dfs(i, total+nums[i])
            res.pop()
            dfs(i+1, total)
        dfs(0,0)
        return sol

        
            

        