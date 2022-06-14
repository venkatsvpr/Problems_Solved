"""
85. Maximal Rectangle

Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
Example 2:

Input: matrix = [["0"]]
Output: 0
Example 3:

Input: matrix = [["1"]]
Output: 1
 

Constraints:

rows == matrix.length
cols == matrix[i].length
1 <= row, cols <= 200
matrix[i][j] is '0' or '1'.
"""
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # Do the max area in a histogram
        def maxInRow(row):
            maxArea = 0
            stack = [] # [idx,height]
            for idx,height in enumerate(row):
                start = idx
                while (len(stack) > 0 and (stack[-1][1] >= height)):
                    [poppedIdx, poppedHeight] = stack.pop()
                    start = poppedIdx
                    maxArea = max(maxArea, poppedHeight * (idx-poppedIdx))
                stack.append([start, height])
            
            idx = len(row)
            while(len(stack) > 0):
                [poppedIdx, poppedHeight] = stack.pop()
                maxArea = max(maxArea, poppedHeight * (idx - poppedIdx))
            
            return maxArea
        
        # do it for every row add the row content before calling max area in historgram
        maxArea = 0
        runningRow = [0 for i in range(len(matrix[0]))]
        for row in matrix:
            for idx in range(len(matrix[0])):
                if row[idx] != "0":
                    runningRow[idx] += 1
                else:
                    runningRow[idx] = 0
            maxArea = max(maxArea,maxInRow(runningRow))
        return maxArea