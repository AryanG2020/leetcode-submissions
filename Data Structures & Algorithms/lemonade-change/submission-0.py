class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if not bills or bills[0]!=5:
            return False
        myMap={5:0,10:0,20:0}
        for bill in bills:
            if bill==5:
                myMap[5]+=1
            elif bill==10:
                if myMap[5]==0:
                    return False
                else:
                    myMap[5]-=1
                    myMap[10]+=1
            elif bill==20:
                if myMap[10]>0 and myMap[5]>0:
                    myMap[20]+=1
                    myMap[10]-=1
                    myMap[5]-=1
                elif myMap[5]>=3:
                    myMap[20]+=1
                    myMap[5]-=3
                else:
                    return False
        return True



        
        