# Merge Intervals
# https://leetcode.com/problems/merge-intervals/description/
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
        lt = []
        prev_start = -1
        prev_end = -1
        if (len(intervals)==0):
            return lt
        
        
        for index,item in enumerate(intervals):
            l1 = []
            l1.append(item.start)
            l1.append(item.end)
            lt.append(l1)
        
        lt = sorted(lt)
        new_lt = []
        for index,l1 in enumerate(lt):
            (item_start, item_end) = (l1[0],l1[1])

          #  print (index,l1,prev_start,prev_end,item_start,item_end)
            if (index == 0):
                prev_start = item_start
                prev_end = item_end
                continue;
                
            if (item_start == prev_start) and (item_end == prev_end):
                continue;
        
            if (prev_start <= item_start and item_start <= prev_end):
                prev_start = min (prev_start, item_start);
                prev_end = max(prev_end, item_end)
                continue;
            if (item_start <= prev_start <= item_end):
                prev_start = min (prev_start,item_start)
                prev_end = max(prev_end, item_end)
                continue;
            if (prev_start <= item_end <= prev_end):
                prev_start = min(prev_start,item_start)
                prev_end = max(prev_start,item_start)
                continue;
            if (item_start <= prev_end <= item_end):
                prev_start = min(prev_start, item_start)
                prev_end = max(prev_end, item_end)
                continue;
            else:
                l2 =[]
                l2.append(prev_start)
                l2.append(prev_end)
                new_lt.append(l2)
                prev_start = item_start
                prev_end = item_end
                continue;
               
        l2 = []
        l2.append(prev_start)
        l2.append(prev_end)
     #   print (new_lt,l2)
        
        if l2 not in new_lt:
            new_lt.append(l2)
        return new_lt



class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged