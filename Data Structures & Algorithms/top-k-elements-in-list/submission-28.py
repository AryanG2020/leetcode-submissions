class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        arr=[[] for i in range(len(nums)+1)]
       
        for num in nums:
            count[num]=1+count.get(num,0)
        for index,val in count.items(): 
            arr[val].append(index)
        result=[]
        for i in range(len(arr)-1,0,-1):
            for val in arr[i]:
                result.append(val)
                if len(result)==k:
                    return result

        
    
    


        



            


            

            

        
        

        