class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i, j = 0, 1
        n = len(intervals)
        results = []
        results.append(intervals[0])

        while j < n:
            if intervals[j][0] > results[i][1]:
                results.append(intervals[j])
                j +=1
                i +=1
            else:
                results[i][0] = min(results[i][0],intervals[j][0])
                results[i][1] = max(results[i][1],intervals[j][1])
                j +=1
        return results


        