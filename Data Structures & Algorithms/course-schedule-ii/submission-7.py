class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        mymap=defaultdict(list)
        seen=set()
        result=[]
        for crs,pre in prerequisites:
            mymap[crs].append(pre)
        
        def dfs(crs):
            if crs in seen:
                return False
            if crs not in mymap:
                if crs not in result:
                    result.append(crs)
                return True
            seen.add(crs)
            for c in mymap[crs]:
                if not dfs(c):
                    return False
            if crs not in result:
                result.append(crs)
            seen.remove(crs)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return result
        