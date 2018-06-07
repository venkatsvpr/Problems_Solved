"""
221. Maximal Square
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if (len(matrix) == 0):
            return 0
        max_side = 0

        # Create a Dp array
        dp =  matrix[:]

        # If atleast one is set as 1, set the max_side as 1
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                dp[i][j] = int(dp[i][j])
                if (dp[i][j] > 0):
                    max_side = 1

        # Start counting
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if (str(matrix[i][j]) == "1"):
                    # Check the minimum of (i-1,j)  (i-1,j-1) (i,j-1) plus one if matrix(i,j) is one.
                    dp[i][j] = 1+ min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])
                    max_side = max(max_side,dp[i][j])
                elif (str(matrix[i][j]) == "0"):
                    # If it is zero. set dp[i][j] to zero
                    dp[i][j] = 0

        # Return the Area as max_side*max_side
        return (max_side*max_side)
    
