class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seen=set()
        adjmap=defaultdict(list)
        res=0
        for n1,n2 in edges:
            adjmap[n1].append(n2)
            adjmap[n2].append(n1)

        def dfs(n):
            if n in seen or n==[]:
                return 
            seen.add(n)
            for nei in adjmap[n]:
                if nei not in seen:
                    dfs(nei)
            return 


        for i in range(n):
            if i not in seen:
                dfs(i)
                res+=1
        return res




        