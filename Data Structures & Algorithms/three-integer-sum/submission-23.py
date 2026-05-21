class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()

        for i, val in enumerate(nums):
            if val>0:
                break
            if i>0 and val==nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                ans=val+nums[l]+nums[r]
                if ans<0:
                    l+=1
                elif ans>0:
                    r-=1
                else:
                    res.append([val, nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l<len(nums) and nums[l]==nums[l-1]:
                        l+=1
                    while r>0 and nums[r]==nums[r+1]:
                        r-=1
        return res





        