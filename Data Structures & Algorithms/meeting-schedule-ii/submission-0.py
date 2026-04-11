"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted(intervals, key = lambda x: x.start)
        end = sorted(intervals, key = lambda x: x.end)
        used = result = i = j = 0
        while i<len(start):
            if(start[i].start < end[j].end):
                used += 1
                i += 1
            else:
                used -= 1
                j += 1
            result = max(result, used)

        
        return result
            
        

        