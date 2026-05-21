class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea=0
        if not grid:
            return 0
        rows,cols=len(grid), len(grid[0])
        visited=set()
        directions=[[1,0],[-1,0],[0,1],[0,-1]]

        def bfs(r,c):
            q=deque()
            q.append((r,c))
            visited.add((r,c))
            area=1
            while q:
                r,c=q.popleft()
                for dr,dc in directions:
                    row=r+dr
                    col=c+dc
                    if row in range(rows) and col in range(cols) and (row,col) not in visited and grid[row][col]==1:
                        area+=1
                        visited.add((row,col))
                        q.append((row,col))
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visited:
                    maxArea=max(maxArea,bfs(r,c))
                    
        return maxArea

        