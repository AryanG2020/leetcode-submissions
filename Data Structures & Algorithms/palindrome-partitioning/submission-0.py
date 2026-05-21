class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def isPalin(word):
            return word == word[::-1]

        def dfs(start):
            if start == len(s):
                res.append(path.copy())
                return

            for end in range(start, len(s)):
                if isPalin(s[start:end+1]):
                    path.append(s[start:end+1])
                    dfs(end + 1)
                    path.pop()

        dfs(0)
        return res

        

            

        
        
        
        
        