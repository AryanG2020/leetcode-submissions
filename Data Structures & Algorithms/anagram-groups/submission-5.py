class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]
        myMap=defaultdict(list)
        for word in strs:
            index=[0]*26
            for char in word:
                diff=ord(char)-ord('a')
                index[diff]+=1
            myMap[tuple(index)].append(word)
        for index, value in myMap.items():
            res.append(myMap[index])
        return res

            

        


 
        



        

        
            
        
        