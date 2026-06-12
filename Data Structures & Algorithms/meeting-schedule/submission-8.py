"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        

        if not intervals:
            return True
        
        intervals.sort(key= lambda x : x.start)
        prev = intervals[0]

        for times in intervals[1:]: 

            if times.start < prev.end: 
                return False

            prev = times
        return True







