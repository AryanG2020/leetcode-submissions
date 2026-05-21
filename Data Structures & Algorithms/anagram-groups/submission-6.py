class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mymap=defaultdict(list)
        for word in strs:
            n=[0]*26
            for char in word:
                n[ord(char)-ord('a')]+=1
            mymap[tuple(n)].append(word)
        res=[]
        for items in mymap.values():
            res.append(items)
        return res


        