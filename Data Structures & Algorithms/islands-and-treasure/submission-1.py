class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #Multi-sourced bfs
        rows,cols=len(grid), len(grid[0])
        INF=2147483647
        q=deque()
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    q.append((r,c))
        while q:
            for _ in range(len(q)):
                r,c=q.popleft()
                for dr, dc in directions:
                    row,col=r+dr,c+dc
                    if row in range(rows) and col in range(cols) and grid[row][col]==INF:
                        q.append((row,col))    
                        grid[row][col]=grid[r][c]+1
        





      
     
        


                
        
        
        