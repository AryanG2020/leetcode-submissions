class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setNum=set()
        for num in nums:
            if num not in setNum:
                setNum.add(num)
            else:
                return True
        return False
        

         