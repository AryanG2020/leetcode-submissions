"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        store=[]
        for interval in intervals:
            store.append([interval.start,1])
            store.append([interval.end,-1])
        store.sort(key=lambda x:(x[0],x[1]))
        count,res=0,0
        for time in store:
            count+=time[1]
            res=max(count,res)
        return res

        