class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap={}
        for i in range(len(nums)):
            find=target-nums[i]
            if find in prevMap:
                return [prevMap[find], i]
            else:
                prevMap[nums[i]]=i
        

       


        
            

            
        