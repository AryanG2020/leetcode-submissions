class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap={}
        seen=set()
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(x):
            if x in seen:
                return False
            if preMap[x]==[]:
                return True 
            seen.add(x)
            for pre in preMap[x]:
                if not dfs(pre):
                    return False
            seen.remove(x)
            preMap[x]=[]
            return True
            
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True




        
        
        