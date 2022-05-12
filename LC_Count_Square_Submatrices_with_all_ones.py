"""
1277. Count Square Submatrices with All Ones

Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

 

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.
 

Constraints:

1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1
"""
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # Here the idea is to count the square submatrices.
        t = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        Ans = 0 
        for x,row in enumerate(matrix):
            for y,item in enumerate(row):
                if x == 0 or y == 0:
                    if matrix[x][y] > 0:
                        t[x][y] = 1
                else:
                    if matrix[x][y] > 0:
                        if t[x-1][y] == 0 or t[x][y-1] == 0 or t[x-1][y-1] ==0:
                            t[x][y] = 1
                        elif (t[x-1][y-1] > 0):
                            t[x][y] = 1 + min(t[x-1][y-1], t[x][y-1], t[x-1][y])
                Ans += t[x][y]
        return Ans
        