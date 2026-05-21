class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=defaultdict(list)
        for items in strs:
            count= [0] *26
            for char in items:
                count[ord(char)-ord('a')]+=1
            result[tuple(count)].append(items)
        return result.values()    
        
        