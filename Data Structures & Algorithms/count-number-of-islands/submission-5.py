class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row,col=len(grid), len(grid[0])
        seen=set()
        res=0
        direction=[[1,0],[-1,0], [0,1], [0,-1]]

        def dfs(r, c):
            if r not in range(row) or c not in range(col) or (r,c) in seen or grid[r][c]=="0":
                return
            if grid[r][c]=="1":
                seen.add((r,c))
                for dr,dc in direction:
                    dfs(r+dr,c+dc)

        for r in range(row):
            for c in range(col):
                if (r,c) not in seen and grid[r][c]=="1":
                    res+=1
                    dfs(r,c)
        return res




        