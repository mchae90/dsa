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
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here
        intervals.sort(key = lambda i : i.start)

        for i in range(len(si) - 2):
            if si[i].end > si[i + 1].start:
                return False
        
        return True

# Key: After sorting the intervals, start time of nth interval will always be <= all the following end time of following intervals
# So just need to compare start time of n to end time of n + 1
# TC: O(logn) + O(n) = O(n)
