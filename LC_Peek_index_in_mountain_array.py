"""
852. Peak Index in a Mountain Array

Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:

Input: [0,1,0]
Output: 1
Example 2:

Input: [0,2,1,0]
Output: 1

3 <= A.length <= 10000
0 <= A[i] <= 10^6
A is a mountain, as defined above.
Approach:
=========
Just do binary search

"""

class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        def rec(start,end,A):
            mid = (start + end)/2
            if (A[mid-1] < A[mid]) and (A[mid] > A[mid+1]):
                return mid
            if (A[mid]-1 < A[mid]):
                return rec(mid,end,A)
            if (A[mid] < A[mid+1]):
                return rec(start,mid,A)
        return (rec (0,len(A)-1,A))
