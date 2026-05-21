class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        while l<r:
            if s[l]!=s[r]:
                leftSkip=s[l+1:r+1]
                rightSkip=s[l:r]
                return leftSkip==leftSkip[::-1] or rightSkip==rightSkip[::-1]
            l,r=l+1,r-1
        return True
        
        
        