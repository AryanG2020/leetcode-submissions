class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=0
        power=10**(len(digits)-1)
        for i in range(len(digits)):
            num=digits[i]*power+num
            power=power//10
        num+=1
        res=[]
        for n in str(num):
            res.append(n)
        return res

        

        