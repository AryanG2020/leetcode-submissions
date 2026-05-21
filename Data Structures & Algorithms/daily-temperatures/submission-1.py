class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[]
        if len(temperatures)==1:
            return 0
        for l in range(len(temperatures)):
            r=l+1
            while r<len(temperatures) and temperatures[l]>=temperatures[r]:
                r+=1
            if r>=len(temperatures):
                ans.append(0)
            else:
                ans.append(r-l)
        return ans

        
