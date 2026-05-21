class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        res=0
        direction=[[1,0],[-1,0],[0,1],[0,-1]]
        row,col=len(grid),len(grid[0])

        def dfs(r,c):
            if r>=row or c>=col or r<0 or c<0 or grid[r][c]=="0":
                return
            if grid[r][c]=="1":
                grid[r][c]="0"
                for dr,dc in direction:
                    r_,c_=dr+r,dc+c
                    dfs(r_,c_)

        
        for i in range(row):
            for j in range(col):
                if grid[i][j]=="1":
                    res+=1
                    dfs(i,j)
        dfs(0,0)
        return res
        