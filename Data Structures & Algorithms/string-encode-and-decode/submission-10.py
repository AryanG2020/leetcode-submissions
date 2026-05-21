class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for items in strs:            
            s+=str(len(items))+"#"+items
        return s
            


    def decode(self, s: str) -> List[str]:
        i=0
        mylist=[]

        while i<len(s):
            j=i
            while s[j]!="#":
                j=j+1
            length= int(s[i:j])
            i=j+1
            j=i+ length
            mylist.append(s[i:j])
            i=j

        return mylist


       
            
                

            

                
                

