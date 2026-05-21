class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        track=set()
        for items in nums:
            if items in track:
                return True
            track.add(items)
        return False

         