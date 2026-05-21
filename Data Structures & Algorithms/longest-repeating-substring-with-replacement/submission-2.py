class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res=0
        l=0
        mymap={}
        for r in range(len(s)):
            mymap[s[r]]=1+mymap.get(s[r],0)

            while (r-l+1-max(mymap.values())>k):
                mymap[s[l]]-=1
                l+=1
            res=max(res, r-l+1)
        return res

            
               

            


        