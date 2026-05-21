class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        visit=set()
        num=[]
        def dfs(r,c):
            if (r,c) in visit:
                return
            if r not in range(row) or c not in range(col) or grid[r][c]==0:
                num.append(1) #see neetcode explanation
                return 
            visit.add((r,c))
            for dr,dc in directions:
                dfs(r+dr,c+dc)

        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    dfs(r,c)
                    break;
        return sum(num)
        