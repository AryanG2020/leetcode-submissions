class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row,col=len(heights), len(heights[0])
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        seenA,seenP=[],[]
        res=[]

        def dfs(r,c,height,seenSet):
            if r not in range(row) or c not in range(col) or heights[r][c]<height or [r,c] in seenSet:
                return
            seenSet.append([r,c])
            for dr,dc in directions:
                dfs(r+dr,c+dc,heights[r][c],seenSet)

        for r in range(row):
            dfs(r,0, heights[r][0],seenP)
            dfs(r,col-1,heights[r][col-1],seenA)
        for c in range(col):
            dfs(0,c,heights[0][c],seenP)
            dfs(row-1,c,heights[row-1][c],seenA)

        for values in seenA:
            if values in seenP:
                res.append(list(values))
        return res

        
        