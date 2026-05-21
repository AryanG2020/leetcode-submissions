class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        string=""
        reverse=""
        for char in s:
            if (char>='a' and char<='z') or (char>='0' and char<='9'):
                string=string+char
                reverse=char+reverse
        return reverse==string
        

        
            
        