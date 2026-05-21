class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjMap=defaultdict(list)
        for ui, vi, ti in times:
            adjMap[ui].append((ti,vi))
        heap=[(0,k)]
        heapq.heapify(heap)
        seen=set()
        res=0

        while heap:
            time, node=heapq.heappop(heap)
            if node in seen:
                continue
            seen.add(node)
            res=time
            for t, dest in adjMap[node]:
                if dest not in seen:
                    heapq.heappush(heap,(t+time,dest))
        return res if len(seen)==n else -1
            


# adjMap= {1:(1,2),2:(1,3),1:(4,4), 3:(1,4)}

        


            



        
        
        