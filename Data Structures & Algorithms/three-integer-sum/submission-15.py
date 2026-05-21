class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol,res=[],[]
        
        def dfs(i,total):
            if total==0 and len(sol)==3 and sorted(sol) not in res:
                res.append(sorted(sol.copy()))
                return
            if i>=len(nums) or len(sol)>3:
                return
            sol.append(nums[i])
            dfs(i+1, total+nums[i])
            sol.pop()
            dfs(i+1,total)
        dfs(0,0)
        return res

        