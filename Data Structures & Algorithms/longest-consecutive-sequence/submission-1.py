class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        longest=0
        count=0
        n=0
        if len(nums)==0:
            return longest 
        
        if len(nums)==1:
            return longest+1 
        while n+1<len(nums):
            
            chain=False
            while (nums[n+1]-nums[n]==1 or nums[n+1]-nums[n]==0):
                if nums[n+1]-nums[n]==1:
                    count+=1
                    chain=True
                n+=1
                if (n+1)==len(nums):
                    break
            if count>longest:
                longest=count
            count=0
            if chain==False:
                n+=1
        return longest+1
            
            

        
        


        