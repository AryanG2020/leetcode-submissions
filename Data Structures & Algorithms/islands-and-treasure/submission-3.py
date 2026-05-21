class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return []
        row,col=len(grid), len(grid[0])
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        INF=2147483647

        def dfs(r,c,dist):
            if r>=row or c>=col or r<0 or c<0 or grid[r][c]==-1:
                return
            if dist>grid[r][c]:
                return
            if dist<grid[r][c]:
                grid[r][c]=dist
            dist+=1
            for dr,dc in directions:
                _r,_c=dr+r, dc+c
                dfs(_r,_c,dist)

        for r in range(row):
            for c in range(col):
                if grid[r][c]==0:
                    dfs(r,c,0)
            

        
        




      
     
        


                
        
        
        