class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        track=[]
        for items in nums:
            if items in track:
                return True
            track.append(items)
        return False

         