"""
253. Meeting Rooms II


Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
"""

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
"""
Approach:
Sort the inputs by start time.
store the end times in a pirority queue. if a start time is greater than the min element.. pop it out and add the new end time in.
else. add it in
the size of Q will tell us how many  rooms are needed
"""
import queue as q
import functools
class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        def cmp (it1, it2):
            return it1.start-it2.start

        Q = q.PriorityQueue()

        if (len(intervals) <= 1):
            return len(intervals)

        maxlen = 0
        # sort the intervals based on the start time
        intervals = sorted(intervals,key=functools.cmp_to_key(cmp))

        # Add the end into a priority Queue
        Q.put(intervals[0].end)

        # for the remaining intervals do thelogic
        for interval in intervals[1:]:
            minEnd = Q.get()
            # Check if there is any overlap
            if (interval.start < minEnd):
                Q.put(minEnd)
            Q.put(interval.end)
            maxlen = max(maxlen, Q.qsize())
        return maxlen


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
"""
Create a Start and End list and add the start and end intervals seperately
Sort both Start and End seperately
Take a Start[s] < End[e],
    If there is no availabilty == 0
        increement the room by one.
    else:
        decrease the availablilty by one
    s += 1
else:
    increase availabilty by one
    e += 1
"""
class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        start = []
        end = []
        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
        start.sort()
        end.sort()
        s = e = avail = maxRoom = 0
        while (s < len(start)):
            if (start[s] < end[e]):
                if (avail == 0):
                    maxRoom += 1
                else:
                    avail -= 1
                s += 1
            else:
                avail += 1
                e += 1
        return maxRoom
