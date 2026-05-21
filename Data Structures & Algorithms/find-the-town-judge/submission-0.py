class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust or n-len(trust)!=1:
            return -1
        for item in trust:
            if item[1]!=trust[0][1]:
                return -1
        return trust[0][1]
        
        
        