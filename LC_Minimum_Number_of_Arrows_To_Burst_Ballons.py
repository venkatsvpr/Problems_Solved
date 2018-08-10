"""
452. Minimum Number of Arrows to Burst Balloons

There are a number of spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter and hence the x-coordinates of start and end of the diameter suffice. Start is always smaller than end. There will be at most 104 balloons.

An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow once shot keeps travelling up infinitely. The problem is to find the minimum number of arrows that must be shot to burst all balloons.

Example:

Input:
[[10,16], [2,8], [1,6], [7,12]]

Output:
2

Explanation:
One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (burstin

Approach:
Sort the ranges
merge subsequent ranges which are overlapping.
O(N log N)
"""

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def in_range(sx,sy,x,y):
            if (sx <= x <= sy):
                #print (" in range ",sx,sy,x,y)
                return True
            if (sx <= y <= sy):
                #print (" in range ",sx,sy,x,y)
                return True
            #print (" not in range ",sx,sy,x,y)
            return False

        points.sort()
        Lt = []
        for [x,y] in points:
            if (len(Lt) == 0):
                Lt.append([x,y])
            else:
                if (in_range(Lt[-1][0],Lt[-1][1],x,y)):
                    Lt[-1] = [max(Lt[-1][0],x) , min(Lt[-1][1],y)]
                else:
                    Lt.append([x,y])
        return len(Lt)
