class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        strs.sort()
        for i in range(len(strs[0])):
            for char in strs:
                if char=="":
                    return ""
                if char[i]!=strs[0][i]:
                    return ans
            ans+=char[i]
        return ans
        