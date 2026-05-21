class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap={}
        for index,val in enumerate(nums):
            if target-val in prevMap:
                return [prevMap[target-val], index]
            else:
                prevMap[val]=index
        
        
            

            
        