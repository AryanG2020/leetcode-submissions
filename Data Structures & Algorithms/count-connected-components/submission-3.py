class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        mymap={i: [] for i in range(n)}
        for x,y in edges:
            mymap[x].append(y)
            mymap[y].append(x)
        notseen=[i for i in range(n)]
        count=[0]

        def dfs(node,parent):
            if parent==-1:
                count[0]+=1
            notseen.remove(node)
            if mymap[node]==[]:
                return
            for nei in mymap[node]:
                if nei==parent:
                    continue;
                if nei in notseen: 
                    dfs(nei,node)
        while notseen:
            dfs(notseen[0],-1)
        return count[0]
                
            
        

        