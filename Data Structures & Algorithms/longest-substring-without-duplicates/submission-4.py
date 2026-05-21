class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check=[]
        maxlength=0
        i=0
        
        while i <len(s):
            if s[i] not in check:
                check.append(s[i])
                i+=1
            else:
                maxlength=max(maxlength, len(check))
                
                while s[i] in check:
                    check.pop(0)       
                check.append(s[i])
                i+=1
        return max(maxlength, len(check))


        