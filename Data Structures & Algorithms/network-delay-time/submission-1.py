import heapq
from collections import defaultdict
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjMap = defaultdict(list)
        
        # Build Adjacency List: Map source -> (transit_time, destination)
        for ui, vi, ti in times:
            adjMap[ui].append((ti, vi))
            
        # Initialize Min-Heap with (cumulative_time, starting_node)
        heap = [(0, k)]
        heapq.heapify(heap) # (Note: A 1-element list is already a valid heap!)
        
        # Tracks nodes whose absolute shortest path is mathematically locked in
        seen = set()
        res = 0

        while heap:
            # Pop the node with the absolute lowest cumulative time currently available
            time, node = heapq.heappop(heap)
            
            # The "Stale Entry" Check: Skip if we found a faster route to this node earlier
            if node in seen:
                continue
                
            # The moment a node survives the check above, its shortest path is guaranteed
            seen.add(node)
            
            # Because the heap pops in increasing order, 'time' is always climbing.
            # The last node processed will naturally dictate the final max time.
            res = time
            
            # Broadcast the signal to all neighbors
            for t, dest in adjMap[node]:
                if dest not in seen:
                    # Push the neighbor + the cumulative time it took to reach here
                    heapq.heappush(heap, (t + time, dest))
                    
        # If our locked-in set size matches 'n', the signal reached the whole network
        return res if len(seen) == n else -1