class Solution:
    def myPow(self, x: float, n: int) -> float:
        def positive_power(x,n):
            if n==0:
                return 1 
            return x*positive_power(x,n-1)
            
        if n>=0:
            return positive_power(x,n)
        else:
            return 1/positive_power(x,-1*n)
        