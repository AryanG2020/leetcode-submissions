class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr=[]
        for l in range(len(nums)):
            find=target-nums[l]
            if find in nums[l+1:]:
                arr.append(l)
                arr.append(nums.index(find,l+1))
                return arr

            

            
        