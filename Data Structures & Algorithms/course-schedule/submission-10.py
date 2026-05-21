class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjMap=defaultdict(list)
        for crs, pre in prerequisites:
            adjMap[crs].append(pre)
        seen=set()
        
        def dfs(crs):
            if adjMap[crs]==[]:
                return True
            elif crs in seen:
                return False
            seen.add(crs)
            for x in adjMap[crs]:
                if not dfs(x):
                    return False
            seen.remove(crs)
            adjMap[crs]=[]
            return True 

        for num in range(numCourses):
            if not dfs(num):
                return False
        return True

            

        