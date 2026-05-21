class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            cur_start, cur_end = res.pop()
            start, end = intervals[i]
            
            if cur_end < start:
                res.append([cur_start, cur_end])
                res.append([start, end])
            elif cur_start > end:
                res.append([start, end])
                res.append([cur_start, cur_end])
            else:
                res.append([
                    min(start, cur_start),
                    max(end, cur_end)
                ])
        
        return res
