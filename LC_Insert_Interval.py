# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        """
        1) Go through the points
        2) If newInterval overlap with the intervals.. update the newInterval.
        """
        Ans = []
        if not intervals:
            lt = [newInterval.start, newInterval.end]
            Ans.append(lt)
            return (Ans)
        is_done = False;
        for points in  intervals:
            if (is_done == True):
                lt = [points.start, points.end]
                Ans.append(lt)
                continue;                
            elif (newInterval.end < points.start):
                lt = [newInterval.start, newInterval.end]
                Ans.append(lt)
                lt = [points.start, points.end]
                Ans.append(lt)
                is_done = True;
            elif (newInterval.start > points.end):
                lt = [points.start, points.end]
                Ans.append(lt)
                continue;           
            else:
                newInterval.start = min (newInterval.start,points.start)
                newInterval.end = max (newInterval.end,points.end)
        if (is_done == False):
            lt = [newInterval.start, newInterval.end]
            Ans.append(lt)
        return (Ans)
