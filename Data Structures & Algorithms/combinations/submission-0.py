class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res,sol=[],[]
        def dfs(n):
            if len(sol)==k and sorted(sol) not in res:
                res.append(sorted(sol.copy()))
                return
            if n<1:
                return
            sol.append(n)
            dfs(n-1)
            sol.pop()
            dfs(n-1)
        dfs(n)
        return res


        