class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mymap={0:1}
        counter=0
        total=0
        for num in nums:
            total+=num
            if total-k in mymap:
                counter+=mymap[total-k]  
            mymap[total]=mymap.get(total,0)+1
            
        return counter





        
        