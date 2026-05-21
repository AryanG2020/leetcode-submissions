class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[]
        if len(temperatures)==1:
            return result.append(0)
        for i in range(len(temperatures)):
            l=i+1
            found=False
            while l<len(temperatures) and temperatures[l]<=temperatures[i]:
                l+=1
            if l>=len(temperatures):
                result.append(0)
            else:
                
                result.append(l-i)
        return result
