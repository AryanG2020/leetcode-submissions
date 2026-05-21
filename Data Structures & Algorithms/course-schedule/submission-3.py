class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        seen=set()
        myMap=defaultdict(list)
        for x,y in prerequisites:
            myMap[x].append(y)
        
        def dfs(c):
            if c in seen:
                return False
            if c not in myMap:
                return True
            seen.add(c)
            for value in myMap[c]:
                if not dfs(value):
                    return False
            seen.remove(c)
           ## myMap.pop(c)
            return True


        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        
        
        