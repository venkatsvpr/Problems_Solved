"""
73. Set Matrix Zeroes

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        def set_row (row_id):
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if (i==row_id):
                        matrix[i][j] = 0
        def set_col (col_id):
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if (j==col_id):
                        matrix[i][j] = 0
        Row = []
        Col = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (matrix[i][j] == 0):
                    Row.append(i)
                    Col.append(j)
        for row in Row:
            set_row (row)
        for col in Col:
            set_col (col)
        return
