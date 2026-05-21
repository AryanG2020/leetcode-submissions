class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for word in strs:
            index=[0]*26
            for char in word:
                index[ord(char)-ord('a')]+=1
            res[tuple(index)].append(word)
        return list(res.values())

 
        



        

        
            
        
        