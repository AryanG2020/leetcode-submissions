class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            counts, countt={}, {}
            for item in s:
                counts[item]=1+counts.get(item,0)
            for item in t:
                    countt[item]= 1+countt.get(item,0)
            return counts==countt    
                


        