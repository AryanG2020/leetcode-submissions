class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, path=[], []
    
        def isPalin(s):
            return s==s[::-1]

        def dfs(start):
            if start== len(s):
                res.append(path.copy())
                return
            for j in range(start, len(s)):
                if isPalin(s[start:j+1]):
                    path.append(s[start:j+1])
                    dfs(j+1)
                    path.pop()
        dfs(0)
        return res
                
        


        