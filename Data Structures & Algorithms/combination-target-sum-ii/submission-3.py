class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sol,res=[],[]
        def dfs(n,total):
            
            if total==target and sorted(sol) not in res:
                res.append(sorted(sol).copy())
                return
            if total>target or n>=len(candidates):
                return
            sol.append(candidates[n])
            dfs(n+1,total+candidates[n])
            sol.pop()
            dfs(n+1,total)
        dfs(0,0)
        return res

            
            

        
        


            

        