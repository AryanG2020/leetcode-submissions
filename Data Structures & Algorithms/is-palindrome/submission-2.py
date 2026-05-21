class Solution:
    def isPalindrome(self, s: str) -> bool:
        reverse=""
        original=""
        s=s.lower()

        
        for char in s:
            if (ord(char)>=97 and ord(char)<=122) or char.isdigit():
                reverse=char+reverse
                original=original+char
        if reverse==original: 
            return True
        return False
            
        