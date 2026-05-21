class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount=Counter(nums)
        heap=[(-val,idx) for idx, val in numCount.items()]
        heapq.heapify(heap)
        output=[]
        while k>0:
            output.append(heapq.heappop(heap)[1])
            k-=1
        return output

        
        
        
        