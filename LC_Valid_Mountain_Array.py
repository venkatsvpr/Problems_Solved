"""
941. Valid Mountain Array

Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[B.length - 1]


Example 1:

Input: [2,1]
Output: false
Example 2:

Input: [3,5,5]
Output: false
Example 3:

Input: [0,3,2,1]
Output: true


Note:

0 <= A.length <= 10000
0 <= A[i] <= 10000

"""

"""
Find the maxIndex and maxNum.
From that point move left and right.. and see it is strictly decresoing,
MaxIndex should not be 0 or the last index.
"""


class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        # If length is less than 3  return false
        if len(A) < 3:
            return False

        maxIndex = -1
        maxNum = float('-inf')
        for i in range(len(A)):
            if (A[i] > maxNum):
                maxNum = A[i]
                maxIndex = i

        if (maxIndex == 0) or (maxIndex == len(A) - 1):
            return False

        tMax = maxNum
        for i in range(maxIndex - 1, -1, -1):
            if (A[i] >= tMax):
                return False
            else:
                tMax = A[i]

        tMax = maxNum
        for i in range(maxIndex + 1, len(A)):
            if (A[i] >= tMax):
                return False
            else:
                tMax = A[i]
        return True