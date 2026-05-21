class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        sol,res=[],[]
        count={}
        for num in nums:
            count[num]=1+count.get(num,0)
        def dfs():
            if len(nums)==len(sol):
                res.append(sol.copy())
                return
            for num in count:
                if count[num]>0:
                    sol.append(num)
                    count[num]-=1
                    dfs()
                    count[num]+=1    
                    sol.pop()
        dfs()
        return res
            
        
        