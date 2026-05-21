class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r= 0, len(numbers)-1

        while l<r:
            if target-numbers[l]-numbers[r]==0:
                return l+1,r+1
            if target -numbers[l]-numbers[r]>0:
                l+=1
            if target-numbers[l]-numbers[r]<0:
                r-=1

        