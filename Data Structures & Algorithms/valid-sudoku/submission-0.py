class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in range(len(board)):
            seen=set()
            for j in range(9):
                if board[row][j]==".":
                    continue
                if board[row][j] in seen or int(board[row][j]) not in range(1,10):
                    return False
                seen.add(board[row][j])
        
        for col in range(len(board[0])):
            seen=set()
            for j in range(9):
                if board[j][col]==".":
                    continue
                if board[j][col] in seen or int(board[j][col]) not in range(1,10):
                    return False
                seen.add(board[j][col])
        
        for square in range(9):
            seen=set()
            for i in range(3):
                for j in range(3):
                    row=(square//3)*3+i
                    col=(square%3)*3+j
                    if board[row][col]==".":
                        continue
                    if row not in range(9) or col not in range(9):
                        break
                    if board[row][col] in seen or int(board[row][col]) not in range(1,10):
                        return False
                    seen.add(board[row][col])
        return True

        


        
        


                
                
            
        