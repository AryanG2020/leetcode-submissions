class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        row,col=len(grid), len(grid[0])
        maxArea=0
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        
        def dfs(r,c,total):
            if r not in range(row) or c not in range(col) or grid[r][c]==0:
                return 0
            if grid[r][c]==1:
                total+=1
                grid[r][c]=0
                for dr,dc in directions:
                    total+=dfs(dr+r,c+dc,0)
            return total 

        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    maxArea=max(maxArea,dfs(r,c,0))
        return maxArea


        