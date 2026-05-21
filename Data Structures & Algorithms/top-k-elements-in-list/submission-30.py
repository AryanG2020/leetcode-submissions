class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap={}
        for num in nums:
            myMap[num]=myMap.get(num,0)+1
        store=[]
        res=[]
        for idx,val in myMap.items():
            store.append((val,idx))
        store.sort()
        while not k==0:
            res.append(store.pop()[1])
            k-=1
        return res

        
    

    

            
        
        
    
    


        



            


            

            

        
        

        