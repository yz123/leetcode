"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
"""

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not newInterval: return intervals
        
        res = [newInterval]
        for interval in intervals:
            #insert into res
            if interval.start < res[-1].start:
                res.insert(-1, interval)
            else:
                res.append(interval)
            
            #check if res[-2].end>=res[-1].end
            #True: merge
            if res[-2].end>=res[-1].start:
                res[-2].end = max(res[-2].end, res[-1].end)
                res.pop()
        
        return res
        
