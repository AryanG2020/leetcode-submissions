class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        
        # Use heapq to get the k most common elements
        return heapq.nlargest(k, count.keys(), key=count.get)

        