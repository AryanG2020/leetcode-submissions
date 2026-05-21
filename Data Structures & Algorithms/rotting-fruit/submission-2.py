class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid), len(grid[0])
        q=deque()
        direction=[[1,0],[-1,0],[0,1],[0,-1]]
        visit=set()
        fresh=0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append((r,c))
                    visit.add((r,c))
                elif grid[r][c]==1:
                    fresh+=1
        minutes=0
        while q and fresh>0:
            for _ in range(len(q)):
                r,c=q.popleft()
                for dr, dc in direction:
                    row,col=r+dr,c+dc
                    if row in range(rows) and col in range(cols) and grid[row][col]==1 and (row,col) not in visit:
                        visit.add((row,col))
                        q.append((row,col))
                        fresh-=1
            minutes+=1
        return  minutes if fresh==0 else -1

                    



        