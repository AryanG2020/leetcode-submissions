class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for items in numbers:
            difference= target-items
            if difference in numbers:
                return [numbers.index(items)+1, numbers.index(difference)+1]
        