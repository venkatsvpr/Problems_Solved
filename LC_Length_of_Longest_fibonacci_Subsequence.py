"""
873. Length of Longest Fibonacci Subsequence
A sequence X_1, X_2, ..., X_n is fibonacci-like if:

n >= 3
X_i + X_{i+1} = X_{i+2} for all i + 2 <= n
Given a strictly increasing array A of positive integers forming a sequence, find the length of the longest fibonacci-like subsequence of A.  If one does not exist, return 0.

(Recall that a subsequence is derived from another sequence A by deleting any number of elements (including none) from A, without changing the order of the remaining elements.  For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].)



Example 1:

Input: [1,2,3,4,5,6,7,8]
Output: 5
Explanation:
The longest subsequence that is fibonacci-like: [1,2,3,5,8].
Example 2:

Input: [1,3,7,11,12,14,18]
Output: 3
Explanation:
The longest subsequence that is fibonacci-like:
[1,11,12], [3,11,14] or [7,11,18].


Note:

3 <= A.length <= 1000
1 <= A[0] < A[1] < ... < A[A.length - 1] <= 10^9
(The time limit has been reduced by 50% for submissions in Java, C, and C++.)

"""
class Solution(object):
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        Approach:
        This is kind of bruteforce.. We fix the first two numbers by iterating
        We check if the third number is present on the set(A) if present we add it to our list
        keep building the list in similar fashion
        we dont have to worry about ordering because this is strictly increasing number and adding two number
        will definetely yield a bigger number.
        """
        maxlen = 0
        s  = set(A)
        for i in range(0,len(A)):
            for j in range(i+1,len(A)):
                a = A[i]
                b = A[j]
                length = 2
                while (a+b in s):
                    length += 1
                    c = a+b
                    a = b
                    b = c
                maxlen = max(maxlen,length)
        if (maxlen > 2):
            return maxlen
        else:
            return 0
