class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        mymap={i:[]for i in range(numCourses)}
        ans=[]
        seen=set()
        for course, pre in prerequisites:
            mymap[course].append(pre)
        
        def dfs(i):
            if i in seen:
                return False
            if mymap[i]==[]:
                if i not in ans:
                    ans.append(i)
                return True
            seen.add(i)
            for pre in mymap[i]:
                if not dfs(pre):
                    return False
            if i not in ans:
                ans.append(i)
            seen.remove(i)
            return True
    
        for i in range(numCourses):
            if not dfs(i):
                return []
        return ans
        
        
        

       