class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count={}
        for items in nums:
            count[items]=count.get(items, 0)+1
            
        
        # Use heapq to get the k most common elements
        return heapq.nlargest(k, count.keys(), key=count.get)

        