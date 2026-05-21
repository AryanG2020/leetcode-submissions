class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myset=set()
        l,r=0,0
        longest=0
        while r<len(s):
            while s[r] in myset:
                myset.remove(s[l])
                l+=1
            myset.add(s[r])
            longest=max(longest, len(myset))
            r+=1
        return longest




        
            

        
     





                

                



        