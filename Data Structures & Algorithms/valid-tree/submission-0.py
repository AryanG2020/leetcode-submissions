class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False
        mymap={i:[] for i in range(n)}
        for edge in edges:
            mymap[edge[0]].append(edge[1])
            mymap[edge[1]].append(edge[0])
        seenset=set()
        
        def dfs(node, parent):
            if node in seenset:
                return False 
            seenset.add(node)
            for nei in mymap[node]:
                if nei==parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        return dfs(0,-1) and len(seenset)==n 
            
            


        
        
        