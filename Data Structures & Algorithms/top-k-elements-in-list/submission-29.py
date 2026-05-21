class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for num in nums:
            count[num]=1+count.get(num, 0)
        arr=[]
        for index, val in count.items():
            arr.append((val, index))
        arr.sort()
        res=[]
        while not k==0:
            res.append(arr.pop()[1])
            k-=1
        return res

            
        
        
    
    


        



            


            

            

        
        

        