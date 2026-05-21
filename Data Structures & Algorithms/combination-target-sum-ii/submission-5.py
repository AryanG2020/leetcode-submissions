class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol =[],[]
        def dfs(i, total):
            if total==target and sorted(sol) not in res:
                res.append(sorted(sol.copy()))
               # return
            if i>=len(candidates):
                return
            sol.append(candidates[i])
            dfs(i+1,total+candidates[i])
            sol.pop()
            dfs(i+1,total)
        dfs(0,0)
        return res


        