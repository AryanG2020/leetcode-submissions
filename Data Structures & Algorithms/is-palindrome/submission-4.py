class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        reverse=""
        original=""
        for char in s:
            if (char>='a' and char<='z') or (char>='0' and char<='9'):
                reverse=reverse+char
                original=char+original
        return original==reverse


        

        
            
        