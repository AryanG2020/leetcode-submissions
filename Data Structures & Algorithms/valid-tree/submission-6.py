class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjMap=defaultdict(list)
        for e1,e2 in edges:
            adjMap[e1].append(e2)
            adjMap[e2].append(e1)
        seen=set()
        q=deque([(0,-1)])
        while q:
            node, parent= q.popleft()
            if node in seen:
                return False 
            seen.add(node)
            for nei in adjMap[node]:
                if nei !=parent:
                    q.append([nei,node])
        return len(seen)==n


       
        