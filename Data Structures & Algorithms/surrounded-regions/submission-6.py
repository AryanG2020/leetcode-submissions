class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row, col= len(board), len(board[0])
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        
        def dfs(r,c):
            if r not in range(row) or c not in range(col) or board[r][c]!="O":
                return
            board[r][c]="#"
            for dr, dc in directions:
                dfs(r+dr,c+dc)
        
        for i in range(row):
            if board[i][col-1]=="O":
                dfs(i,col-1)
            if board[i][0]=="O":
                dfs(i,0)
        for j in range(col):
            if board[0][j]=="O":
                dfs(0,j)
            if board[row-1][j]=="O":
                dfs(row-1,j)
        for r in range(row):
            for c in range(col):
                if board[r][c]=="#":
                    board[r][c]="O"
                elif board[r][c]=="O":
                    board[r][c]="X"
        


   
        