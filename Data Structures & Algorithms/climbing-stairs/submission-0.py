class Solution:
    def climbStairs(self, n: int) -> int:
        memo={}
        for i in range(1, n+1):
            if i==1:
                result=1
            elif i==2:
                result=2
            else:
                result= memo[i-1]+memo[i-2]
            memo[i]=result
        return memo[i]
        

        