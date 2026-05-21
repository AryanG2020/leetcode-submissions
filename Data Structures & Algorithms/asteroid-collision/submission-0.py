class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans=[]    
        for x in asteroids:
            while ans and x<0 and ans[-1]>0:
                diff=ans[-1]+x
                if diff>0:
                    x=0
                elif diff<0:
                    ans.pop()
                else:
                    ans.pop()
                    x=0
            if x:
                ans.append(x)
        return ans
        

        
        