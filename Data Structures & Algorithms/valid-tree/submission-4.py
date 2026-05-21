class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjmap=defaultdict(list)
        if not edges:
            return True
        for v1,v2 in edges:
            adjmap[v1].append(v2)
            adjmap[v2].append(v1)
        seen=set()
        q=deque([(edges[0][0],-1)])
        while q:
            node,parent=q.popleft()
            if node in seen:
                return False
            seen.add(node)
            for nei in adjmap[node]:
                if nei==parent:
                    continue
                q.append([nei,node])
        return len(seen)==n

        
        