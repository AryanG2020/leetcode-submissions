class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        row,col=len(grid),len(grid[0])
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        res=0
        def dfs(r,c,area):
            if r>=row or c>=col or r<0 or c<0 or grid[r][c]==0:
                return area
            area+=1
            grid[r][c]=0
            for dr, dc in directions:  
                area= dfs(dr+r,dc+c,area)
            return area
                
        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    res=max(res,dfs(r,c,0))
        return res
        