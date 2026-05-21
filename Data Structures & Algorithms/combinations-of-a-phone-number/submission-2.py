class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        
        mymap={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        def dfs(idx, sol):
            if len(sol)==len(digits):
                res.append(sol)
                return
            for c in mymap[digits[idx]]:
                dfs(idx+1, sol+c)         

        if digits:
            dfs(0,"")
        return res


        