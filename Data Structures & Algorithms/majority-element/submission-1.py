class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mymap={}
        for num in nums:
            mymap[num]=1+mymap.get(num,0)
        maxVal=max(mymap.values())
        for key, val in mymap.items():
            if maxVal==val:
                return key

        