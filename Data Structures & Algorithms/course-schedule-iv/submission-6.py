class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        pre={i:[] for i in range(numCourses) }
    
        for pr,crs in prerequisites:
            pre[crs].append(pr)
        res=[]

        def dfs(course):
            if course not in preMap:
                preMap[course]=set()
                for preq in pre[course]:
                    preMap[course] = preMap[course].union(dfs(preq))  # assign new set
                preMap[course].add(course)
            return preMap[course]

            
        preMap={}
        for x in range(numCourses):
            dfs(x)

        for pr,crs in queries:
            res.append(pr in preMap[crs])
           
        return res


        

        