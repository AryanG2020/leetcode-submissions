class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        i=0
        for i in range(2):
            for num in nums:
                ans.append(num)
            i+=1
        return ans

        