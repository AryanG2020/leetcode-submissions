class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start= 0
        end= len(nums)-1

        found=False
        while start<=end and found==False:
            middle= int((start+end)/2)
            if target==nums[middle]:
                found=True
            elif target>nums[middle]:
                start=middle+1
            elif target<nums[middle]:
                end=middle - 1
            
        if found==True:
            return middle
        else:
            return -1
        

        