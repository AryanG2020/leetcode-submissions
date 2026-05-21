class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr=[1] * len(nums) 
        prod=1
        zero=0
        
        for i in range(0,len(nums)):
            if nums[i]!=0:
                prod= nums[i]  * prod
            else:
                zero+=1
        if zero>1: 
                arr=[0] * len(nums)
                return arr
            

        for i in range(0, len(nums)):
            
            if nums[i]==0:
                arr[i]=prod
                
            elif zero==0:
                arr[i]= int(prod/nums[i])
            else:
                arr[i]=0

        return arr




        