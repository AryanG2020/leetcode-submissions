class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        q=collections.deque()
        row,col=len(grid),len(grid[0])
        fresh=0
        time=0
        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    fresh+=1
                elif grid[r][c]==2:
                    q.append((r,c))

        while q and fresh>0:
            for x in range(len(q)):
                r,c=q.popleft()
                for dr,dc in directions:
                    _r,_c=r+dr,c+dc
                    if _r in range(row) and _c in range(col) and grid[_r][_c]==1:
                        q.append((_r,_c))
                        grid[_r][_c]=2
                        fresh-=1
            time+=1
        return time if fresh==0 else -1



       
        





                    




        
        
        

                    



        