class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        subset=[]
        def dfs(counter):
            if counter==len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[counter])
            dfs(counter+1)
            subset.pop()
            dfs(counter+1)
        dfs(0)
        return res
      
    


        
        




        