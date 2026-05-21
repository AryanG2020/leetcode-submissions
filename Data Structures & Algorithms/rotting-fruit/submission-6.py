class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols=len(grid), len(grid[0])
        res=0
        fresh=0
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        queue=deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    queue.append((r,c))
                elif grid[r][c]==1:
                    fresh+=1
        
        while queue and fresh>0:
            for _ in range(len(queue)):
                r,c=queue.popleft()          
                for dr,dc in directions:
                    row,col=r+dr,c+dc
                    if row in range(rows) and col in range(cols) and grid[row][col]==1:
                        queue.append((row,col))
                        grid[row][col]=2
                        fresh-=1
            res+=1
        
        return res if fresh==0 else -1
                


        
                    



        

 

