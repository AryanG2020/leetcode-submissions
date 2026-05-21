class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myMap=set(nums)
        longest=0
        for num in myMap:
            if num-1 not in myMap:
                length=1
                while num+1 in myMap:
                    length+=1
                    num+=1
                longest =max(longest, length)
            length=0
        return longest
            

        
        
            

                
                
       
            



        
            
            

        
        


        