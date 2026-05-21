class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # THE FLEX: This single line catches the "Floating Islands" bug, 
        # the "Empty Array" bug, and guarantees no extra cycles exist!
        if len(edges) != n - 1:
            return False
            
        adjmap = defaultdict(list)
        for v1, v2 in edges:
            adjmap[v1].append(v2)
            adjmap[v2].append(v1)
            
        seen = set()
        # Always safe to start at node 0
        q = deque([(0, -1)])
        
        while q:
            node, parent = q.popleft()
            if node in seen:
                return False
            seen.add(node)
            for nei in adjmap[node]:
                if nei == parent:
                    continue
                q.append((nei, node))
                
        return len(seen) == n