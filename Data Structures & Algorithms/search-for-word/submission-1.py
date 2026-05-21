class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m=len(board)
        n=len(board[0])
        if m==1 and n==1:
            return board[0][0]==word

        def backtrack(i, x, y):
            if i==len(word):
                return True
            if x<0 or x>=m or y<0 or y>=n or board[x][y]!=word[i]:
                return False
            char=board[x][y]
            board[x][y]="#"

            for x_add, y_add in [(1,0),(-1,0),(0,1),(0,-1)]:
                r,c=x+x_add, y+y_add
                if 0<=r<m and 0<=c<n:
                    if backtrack(i+1,r,c): 
                        return True
            board[x][y]=char
            return False
        
        for x in range(m):
            for y in range(n):
                if backtrack(0, x,y):
                    return True
        return False
                
        