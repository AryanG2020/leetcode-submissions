class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        mylist=[]
        for point in points:
            dist=point[0]**2+point[1]**2
            mylist.append((dist,[point[0],point[1]]))
        heapq.heapify(mylist)
        ans=[]
        while k>0:
            ans.append(heapq.heappop(mylist)[1])
            k-=1
        return ans



        