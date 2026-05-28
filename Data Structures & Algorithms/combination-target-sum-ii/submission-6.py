class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sol, res=[],[]
        candidates.sort()
        def dfs(n, total):
            if target==total:
                res.append(sol.copy())
                return 
            for i in range(n, len(candidates)):
                if i>n and candidates[i]==candidates[i-1]:
                    continue 
                if total+candidates[i]>target:
                    break 
                sol.append(candidates[i])
                dfs(i+1, total+candidates[i])
                sol.pop()
        dfs(0,0)
        return res 

        