class Solution:
    def isValid(self, s: str) -> bool:

        stk=[]
        maps={"}":"{", ")":"(", "]":"["}
        for char in s:
            if char not in maps:
                stk.append(char)
            elif len(stk)==0 or stk[-1]!=maps[char]:
                return False
            else:
                stk.pop()
        return len(stk)==0

          

        