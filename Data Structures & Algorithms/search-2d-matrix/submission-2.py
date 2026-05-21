class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for row in matrix:
            if target >=min(row) and target<=max(row):
                l=0
                r=len(row)-1
                while l<=r:
                    middle=l+(r-l)//2
                    if row[middle]==target:
                        return True
                    elif row[middle]<target:
                        l=middle+1
                    else:
                        r=middle-1
                return False 
        return False

                    
        


        