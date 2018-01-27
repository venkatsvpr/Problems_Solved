"""
Start from the end of the firs row.
go one row down if the value is greater than targe
go one row left if the value is less than  target
"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if (matrix is None):
            return False
        
        if ((0 == len(matrix)) or (0 == len(matrix[0]))):
            return False
        
        row_length = len(matrix)
        col_length = len(matrix[0])

        if (row_length == 1):
            if target in matrix[0]:
                return True
            else:
                return False
            
        i = 0;
        j = col_length-1
        while ((i<row_length) and (j>=0)):
            element = matrix[i][j]
            if (element == target):
                return True
            
            if (element < target):
                i += 1
                continue;
            
            if (element > target):
                j -= 1
                continue;
        
        return False
