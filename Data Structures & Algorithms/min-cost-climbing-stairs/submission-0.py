class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache={}
        for i in range(len(cost)+1):
            if i<2:
                result=0 
            else:
                result=min(cache[i-1]+cost[i-1],cache[i-2]+cost[i-2])
            cache[i]=result
        return cache[len(cost)]
        