class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        zero_rows = set()
        zero_cols = set()

        # First pass: find all rows and columns that need to be zeroed
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)

        # Second pass: zero out rows
        for r in zero_rows:
            for c in range(cols):
                matrix[r][c] = 0

        # Third pass: zero out columns
        for c in zero_cols:
            for r in range(rows):
                matrix[r][c] = 0


        
        