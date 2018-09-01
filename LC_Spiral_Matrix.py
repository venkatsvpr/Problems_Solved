"""
54. Spiral Matrix


Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]


"""

"""
Approach:
========
This is an intersting one.. looks tricky..
approach the problem layer by layer.. use a generator to genrate points to visit..
move one layer deeper. continue doing this.
"""
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # Yield points for a layer
        def get_nxt (r1,c1,r2,c2):
            for c in range(c1,c2+1):
                yield r1,c
            for r in range(r1+1,r2+1):
                yield r,c2
            if (r2 > r1) and (c2 > c1):
                for c in range(c2-1,c1-1,-1):
                    yield r2,c
                for r in range(r2-1,r1,-1):
                    yield r,c1
        Ans = []
        if not matrix:
            return Ans
        r1 = c1 = 0
        r2 = len(matrix)-1
        c2 = len(matrix[0])-1
        while (c1 <= c2) and (r1 <= r2):
            for x,y in get_nxt(r1,c1,r2,c2):
                Ans.append(matrix[x][y])
            # Move one layer inside
            c1 += 1
            r1 += 1
            c2 -= 1
            r2 -= 1
        return Ans
                
