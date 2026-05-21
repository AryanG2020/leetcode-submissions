class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        mymap=defaultdict(list)
        res=[]
        for crs, pre in prerequisites:
            mymap[crs].append(pre)
        seen,cycle=set(), set()
        
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in seen:
                return True 
            cycle.add(crs)
            for x in mymap[crs]:
                if not dfs(x):
                    return False
            seen.add(crs)
            cycle.remove(crs)
            res.append(crs)
            return True


        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
        





        

        