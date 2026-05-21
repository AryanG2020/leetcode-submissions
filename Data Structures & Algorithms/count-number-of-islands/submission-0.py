class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        visited=set()
        row, col= len(grid), len(grid[0])
        island=0

        def bfs(r,c):
            q=deque()
            direction=[[0,1],[1,0],[0,-1],[-1,0]]
            q.append((r,c))
            while q:
                row_pop,col_pop=q.popleft()
                for dr, dc in direction:
                    _r=row_pop+dr
                    _c=col_pop+dc
                    if _r in range(row) and _c in range(col) and (_r,_c) not in visited and grid[_r][_c]=='1':
                        q.append((_r,_c))
                        visited.add((_r,_c))

        for r in range(row):
            for c in range(col):
                if grid[r][c]=='1' and (r,c) not in visited:
                    visited.add((r,c))   
                    bfs(r,c)
                    island+=1
        return island

        