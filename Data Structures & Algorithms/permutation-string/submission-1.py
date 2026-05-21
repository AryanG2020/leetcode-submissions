class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=0
        r=l+len(s1)-1
        maps1={}
        maps2={}
        for char in s1:
            maps1[char]=1+maps1.get(char, 0)
        while r<len(s2):
            for char in s2[l:r+1]:
                maps2[char]=1+maps2.get(char,0)
            if maps1==maps2:
                return True 
            else:
                maps2={}
                l+=1
                r+=1
        return False

        
        