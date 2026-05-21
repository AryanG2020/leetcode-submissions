
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        result=[]
        def validParan(openN, closedN):
            if openN==closedN==n:
                result.append("".join(stack))
                return
            if openN<n:
                stack.append("(")
                validParan(openN+1, closedN)
                stack.pop()
            if openN>closedN:
                stack.append(")")
                validParan(openN, closedN+1)
                stack.pop()
            
        validParan(0,0)
        return result


                
        
