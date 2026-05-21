class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row,col=len(board),len(board[0])
        direction=[[0,1],[0,-1],[1,0],[-1,0]]
        seen=set()
        if row==1 and col==1:
            return board[0][0]==word

        def dfs(r,c,i):
            if i==len(word):
                return True
            if r>=row or c>=col or r<0 or c<0 or word[i]!=board[r][c] or (r,c) in seen:
                return False
            seen.add((r,c))
            for dr,dc in direction:
                if 0<=dr+r<row and 0<=dc+c<col and dfs(r+dr,c+dc,i+1): 
                    return True
            seen.remove((r,c))
            return False
                    

        for r in range(row):
            for c in range(col):
                if (r,c) not in seen and dfs(r,c,0):
                    return True
        return False

        
        