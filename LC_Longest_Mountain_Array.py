"""
Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

    B.length >= 3
    There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]

(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain.

Return 0 if there is no mountain.

Example 1:

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.

Example 2:

Input: [2,2,2]
Output: 0
Explanation: There is no mountain.

Note:

    0 <= A.length <= 10000
    0 <= A[i] <= 10000
"""

class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int

        Up-hill
        Down-hill
        """
        peeks = []
        def move_both_ways(j):
            right = j
            left = j
            for i in range(j,len(A)-1):
                if (A[i] > A[i+1]):
                    right = i+1
                    continue;
                else:
                    break;
            for i in range(j,0,-1):
                if (A[i] > A[i-1]):
                    left = i-1
                    continue
                else:
                    break
            return left,right

        for i in range(1,len(A)-1):
            if (A[i-1] < A[i]) and (A[i] >  A[i+1]):
                left,right = move_both_ways(i)
                maxLen = max(maxLen, right-left+1)
        return (maxLen)
