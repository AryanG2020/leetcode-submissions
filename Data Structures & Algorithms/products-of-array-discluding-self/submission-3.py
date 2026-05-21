class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix=[1]*len(nums),[1]*len(nums)
        t1, t2=1,1
        res=[]
        for i in range(len(nums)):
            if i==0:
                continue
            else:
                t1=t1*nums[i-1]
                prefix[i]=t1
        
        for j in range(len(nums)-1,-1,-1):
            if j==len(nums)-1:
                continue
            else:
                t2=t2*nums[j+1]
                postfix[j]=t2
        for i in range(len(nums)):
            res.append(prefix[i]*postfix[i])
        return res

    
        
            
        