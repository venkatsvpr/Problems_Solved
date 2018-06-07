"""
85. Maximum Rectangle
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
"""
class Solution(object):
    max_area = 0
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        # Find the max_area of a row. Similar to max area histogram
        def find_max_row(heights):
            stack = [-1]
            heights.append(0)
            # Store the index of heights in stack. If a height less than the
            # last element in stack, then pop the stack.
            for i in range(len(heights)):
                while (heights[stack[-1]] > heights[i]):
                    height = heights[stack.pop()]
                    width = i - stack[-1] -1
                    # calculate the max area
                    self.max_area = max(self.max_area, height*width)
                stack.append(i)
            heights.pop()
            return

        # Convert String "1" to Integer 1
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])

        # If the length is zero return zero
        if (len(matrix) == 0):
            return 0

        # If a matrix[i][j] is one .. add the matrix[i-1][j]
        # If matrix[i][j] is zero then set matrix[i][j] as zero
        self.max_area = 0
        find_max_row(matrix[0])
        for i in range(1,len(matrix)):
            for j in range(0,len(matrix[0])):
                if (matrix[i][j] == 1):
                    matrix[i][j] = 1 + matrix[i-1][j]
                elif (matrix[i][j] == 0):
                    matrix[i][j] = 0
            find_max_row(matrix[i])

        # Return max_area
        return self.max_area


                
