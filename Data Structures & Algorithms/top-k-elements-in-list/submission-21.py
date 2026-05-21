class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        freq=[[] for i in range(len(nums)+1)]
        result=[]
        for item in nums:
            count[item]= 1+ count.get(item, 0)
        for key, val in count.items():
            freq[val].append(key)

        for array in range(len(freq)-1,0,-1):
                    for n in freq[array]:
                        result.append(n)
                        if len(result)==k:
                            return result



            


            

            

        
        

        