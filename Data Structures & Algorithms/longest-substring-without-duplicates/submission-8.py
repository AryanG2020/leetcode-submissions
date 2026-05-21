class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myset= set()
        result=0
        l=0
        for r in range(len(s)):
            while s[r] in myset:
                myset.remove(s[l])
                l+=1
            result=max(result, r-l+1)
            myset.add(s[r])
        return result





                

                



        