"""
302. Smallest Rectangle Enclosing Black Pixels

You are given an m x n binary matrix image where 0 represents a white pixel and 1 represents a black pixel.

The black pixels are connected (i.e., there is only one black region). Pixels are connected horizontally and vertically.

Given two integers x and y that represents the location of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.

You must write an algorithm with less than O(mn) runtime complexity

 

Example 1:


Input: image = [["0","0","1","0"],["0","1","1","0"],["0","1","0","0"]], x = 0, y = 2
Output: 6
Example 2:

Input: image = [["1"]], x = 0, y = 0
Output: 1
 

Constraints:

m == image.length
n == image[i].length
1 <= m, n <= 100
image[i][j] is either '0' or '1'.
0 <= x < m
0 <= y < n
image[x][y] == '1'.
The black pixels in the image only form one component.

"""
class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        def searchCol(start, end, startRow, endRow, zeroToOne):
            while (start != end):
                mid = start + ( end - start)//2
                idx = startRow
                while(idx < endRow and image[idx][mid] == "0"):
                    idx += 1
                blackFound = idx < endRow
                
                # If we find black and we are looking for black. look current left
                if blackFound == zeroToOne:
                    end = mid
                # If not look right
                else:
                    start = mid +1
            return start
        def searchRow(startCol, endCol, start, end, zeroToOne):
            while (start != end):
                mid = start + ( end - start)// 2
                idx = startCol
                while(idx < endCol and image[mid][idx] == "0"):
                    idx += 1
                blackFound = idx < endCol
                # If we find black and we are looking for black. look up
                if blackFound == zeroToOne:
                    end = mid
                # If not look down
                else:
                    start = mid+1
            return start
        m = len(image)
        n = len(image[0])
        # find the left and right points
        left = searchCol(0,y,0,m,True)
        right = searchCol(y+1,n,0,m,False)
        # find the top and bottom points.
        top = searchRow(left, right,0,x,True)
        bottom = searchRow(left,right,x+1,m,False)
        # find area
        return (right -left ) * (bottom-top)