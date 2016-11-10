"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals: return intervals
        
        intervals = sorted(intervals, key = lambda x: x.start)
        result = [intervals[0]]
        for i in xrange(1, len(intervals)):
            first = result[-1]
            second = intervals[i]
            if first.end >=second.start:
                result[-1].end = max(first.end, second.start, second.end)
            else:
                result.append(intervals[i])
        return result
            
        
