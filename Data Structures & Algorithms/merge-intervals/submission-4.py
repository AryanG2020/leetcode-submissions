class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res=[]
        res.append(intervals[0])
        for interval in intervals[1:]:
            prev=res[-1]
            if interval[0]<=prev[1]:
                res[-1][1]=max(prev[1],interval[1])
            else:
                res.append(interval)
        return res




        