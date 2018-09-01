"""

891. Sum of Subsequence Widths

Given an array of integers A, consider all non-empty subsequences of A.

For any sequence S, let the width of S be the difference between the maximum and minimum element of S.

Return the sum of the widths of all subsequences of A.

As the answer may be very large, return the answer modulo 10^9 + 7.



Example 1:

Input: [2,1,3]
Output: 6
Explanation:
Subsequences are [1], [2], [3], [2,1], [2,3], [1,3], [2,1,3].
The corresponding widths are 0, 0, 0, 1, 1, 2, 2.
The sum of these widths is 6.


Note:

1 <= A.length <= 20000
1 <= A[i] <= 20000


"""
"""
Intuition:
Lets supppose we sort the numbers.
1,2,3,4

We are at  A[i], there are 2^i in which A[i] will be maximum
And there 2^(n-i-1) in which A[i] will be minimum
[1] [2] [3]
[1,2] [2,3]  [ 1,3]
[1,2,3]

lets take 3 it is at i=2
there are four in which it is max
[2,3] [1,3] [1,2,3] [3]
and one in which is its minmum
[3]

Lets take 2...  i = 1
there are two in which it is max
[2] [1,2]
There are  two in which it is min
[2] [2,3]

Lets take 3 .... i = 0
max [1]
min  [1] [1,2] [1,3] [1,23]
"""
class Solution(object):
    def sumSubseqWidths(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        def pow2(i):
            return (1<<i)

        res = 0
        A.sort()
        for i in range(len(A)):
            res += A[i] * (pow2(i))
            res -= A[i] * (pow2(len(A)-i-1))
        return res%((10**9)+7)
