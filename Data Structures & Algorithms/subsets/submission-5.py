class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, ans=[],[]
        def dfs(n):
            if n==len(nums):
                res.append(ans.copy())
                return 
            ans.append(nums[n])
            dfs(n+1)
            ans.pop()
            dfs(n+1)
        dfs(0)
        return res
      