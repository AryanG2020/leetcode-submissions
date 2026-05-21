class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r=0, len(numbers)-1
        ans=[]
        while numbers[l]+numbers[r]!=target:
            add=numbers[l]+numbers[r]
            if target-add>0:
                l+=1
            else:
                r-=1
        return [l+1,r+1]
            
            

       
                


        
       
        