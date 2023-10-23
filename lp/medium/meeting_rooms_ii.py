from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here
        res = []

        intervals.sort(key = lambda x: x.start)
        res.append([intervals[0]])

        for i in range(1, len(intervals)):
            position = -1
            for j in range(len(res)):
                if res[j][-1].end <= intervals[i].start:
                    position = j
            if position == -1:
                res.append([intervals[i]])
            else:
                res[position].append(intervals[i])

        return len(res)   
    
from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here
        start = []
        end = []

        for i in range(len(intervals)):
            start.append(intervals[i].start)
            end.append(intervals[i].end)
        
        start.sort()
        end.sort()

        count = 0
        res = 0

        s, e = 0, 0

        while s < len(start) and e < len(end):
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            res = max(res, count)

        return res
    
    # [(0,30),(5,10),(15,20)]