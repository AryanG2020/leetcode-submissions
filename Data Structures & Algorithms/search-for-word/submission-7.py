class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        direction=[[0,1],[0,-1],[1,0],[-1,0]]
        rows,cols=len(board), len(board[0])
        
        def dfs(r,c,i):
            if i==len(word):
                return True
            if r not in range(rows) or c not in range(cols) or board[r][c]=="#" or word[i]!=board[r][c]:
                return False
            board[r][c]="#"
            for dr, dc in direction:
                if dfs(dr+r,c+dc,i+1):
                    return True
            board[r][c]=word[i]
        
        for i in range(rows):
            for j in range(cols):
                if dfs(i,j,0):
                    return True
        return False

        