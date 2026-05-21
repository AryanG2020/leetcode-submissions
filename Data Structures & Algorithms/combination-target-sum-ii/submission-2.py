class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sol, res=[],[]
        def dfs(counter):
            if sum(sol)==target and sorted(sol) not in res:
                res.append(sorted(sol).copy())
                return 
            if counter==len(candidates):
                return
            sol.append(candidates[counter])
            dfs(counter+1)
            sol.pop()
            dfs(counter+1)
        dfs(0)
        return res


            

        