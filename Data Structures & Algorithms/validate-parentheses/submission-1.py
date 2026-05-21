class Solution:
    def isValid(self, s: str) -> bool:
        maps={'}':'{',']':'[',')':'('}
        stack=[]
        for char in s:
            if char not in maps:
                stack.append(char)
            elif len(stack)==0 or maps[char]!=stack[-1]:
                return False
            else:
                stack.pop()
        return len(stack)==0 



      



          

        