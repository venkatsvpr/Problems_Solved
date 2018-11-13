"""
939. Minimum Area Rectangle


Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.

If there isn't any rectangle, return 0.



Example 1:

Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4
Example 2:

Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2


Note:

1 <= points.length <= 500
0 <= points[i][0] <= 40000
0 <= points[i][1] <= 40000
All points are distinct.


We could do logic comparable to N^2
the core of the logic is to to store the points belonging to a x or y.. pick it based on the number of scuh points..
lets pick x for now..
Have a default dict of list.. with the key as the x values and the list continatin the y values.
sort everything (both keys and the elemetns in the list)
and start processing points one by one..
for two ys.. y1 and y2 for x same.. see if we ahve a pastX entry.. meeaning.. another x value with the same y,... meaning we could form a rectangle..
update the ans by finding min area everytime..
if we are not able ot ifnd such a past value.. add this to pastX registry and keep seeing more points.

"""
import collections


class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        nUniqueX = len(set(x for x, y in points))
        nUniqueY = len(set(y for x, y in points))
        # In this case there could be no rectangles formed since every point
        # is on the same x or y
        if (nUniqueX == n) or (nUniqueY == n):
            return 0

        pt = collections.defaultdict(list)
        # Take one with more count as the index
        if (nUniqueX > nUniqueY):
            for x, y in points:
                pt[x].append(y)
        else:
            for x, y in points:
                pt[y].append(x)

        # Dict to keep track of past (y1,y2) and corresponding x value
        pastX = dict()
        # Ans value assigned to infinity
        Ans = float('inf')

        # Loop through the keys in sorted order
        for x in sorted(pt):
            # sort the list which resides in the thing pointed by x
            pt[x].sort()
            # do a N^2 logic.. if we see a pastX(y1,y2) then find the area.
            # store for every time in pastX
            for i in range(len(pt[x])):
                for j in range(i):
                    y1, y2 = pt[x][j], pt[x][i]
                    if ((y1, y2) in pastX):
                        Ans = min(Ans, abs(y2 - y1) * (x - pastX[(y1, y2)]))
                    pastX[(y1, y2)] = x
        if (Ans == float('inf')):
            return 0
        return Ans