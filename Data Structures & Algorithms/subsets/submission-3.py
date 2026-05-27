class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #myset=()
        res, ans=[[]],[]
        def dfs(n):
            if n==len(nums):
                return 
            ans.append(nums[n])
            res.append(ans.copy())
            dfs(n+1)
            ans.pop()
            dfs(n+1)
        dfs(0)
        return res
        

            
            

        