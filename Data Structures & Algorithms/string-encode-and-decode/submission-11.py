class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=''
        for word in strs:
            encoded=encoded+str(len(word))+"#"+word
        return encoded

    def decode(self, word:str)->List[str]:
        result=[]
        start=0
        while start<len(word):
            i=start
            length=''
            while word[i]!="#":
                length=length+word[i]
                i+=1
            start=i+1
            end=start+int(length)
            result.append(word[start:end])
            start=end
        return result




        
        
             




            
                

            

                
                

