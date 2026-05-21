class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        myset=set(nums)
        longest=0

        for n in myset:
            chain=1
            while n+1 in myset:
                chain+=1
                n+=1
            longest=max(longest, chain)
        return longest
            

                
                
       
            



        
            
            

        
        


        