"""
304. Range Sum Query 2D - Immutable


Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2.

"""
Approach.
Simple logic.. create a ruunning sum...
have a dictionary... and dictionary of (x,y) should conain the sum of the rectaangle from 0,0 to x,y.


rectangle area from x1,y1 to x2,y2 is
= area(0,0 to x2,y2) - (area from 0,0 to x1-1,y2   +  area from x2,y1-1 )  + (area from 00 to x1-1 y1-1)
the last part is subtracted twice so add it.

"""
class NumMatrix(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.arraysum = dict()
        m = len(matrix)
        if (m <= 0):
            return
        n = len(matrix[0])
        rsum = 0
        for i in range(m):
            rsum = 0
            for j in range(n):
                rsum += matrix[i][j]
                self.arraysum[(i,j)] = rsum
                if (i != 0):
                    self.arraysum[(i,j)] += self.arraysum[(i-1,j)]
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        def getFromDict (x, y, dict):
            if (x,y) not in dict:
                return 0
            return dict[(x,y)]
        commonblock = getFromDict (row1-1, col1-1, self.arraysum)
        topblock = getFromDict (row1-1, col2, self.arraysum)
        leftblock = getFromDict (row2, col1-1, self.arraysum)
        wholeblock = getFromDict (row2, col2, self.arraysum)
        return wholeblock  -(topblock + leftblock) + commonblock


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)2
# param_1 = obj.sumRegion(row1,col1,row2,col2)
