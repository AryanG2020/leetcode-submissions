"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #Watch greg hogg's video: https://www.youtube.com/watch?v=wWE7YzuBBkE
        if not node:
            return None
        myMap={}
        stack=[]
        start=node
        stack.append(start)
        while stack:
            node=stack.pop()
            myMap[node]=Node(val=node.val)
            for nei in node.neighbors:
                if nei not in myMap:
                    stack.append(nei)
        for old, new in myMap.items():
            for nei in old.neighbors:
                new.neighbors.append(myMap[nei])

        return myMap[start]


        
        
        
        