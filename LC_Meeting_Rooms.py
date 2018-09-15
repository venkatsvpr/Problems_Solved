"""
252. Meeting Rooms

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Example 1:

Input: [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: [[7,10],[2,4]]
Output: true
"""


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
"""
Approach:
Sort it based on starting time and see if there are any overlaps between subsequent intervals.
if there are overlaps return false
return true
"""
import functools
class Solution:
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        def cmp (it1, it2):
            return it1.start-it2.start
        if (len(intervals) <= 1):
            return True
        intervals = sorted(intervals, key=functools.cmp_to_key(cmp))
        prevStart,prevEnd = intervals[0].start,intervals[0].end
        for interval in intervals[1:]:
            if (interval.start >= prevEnd):
                prevStart,prevEnd = interval.start,interval.end
                continue;
            return False
        return True
        
