"""
960. Delete Columns to Make Sorted III

We are given an array A of N lowercase letter strings, all of the same length.

Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.

For example, if we have an array A = ["babca","bbazb"] and deletion indices {0, 1, 4}, then the final array after deletions is ["bc","az"].

Suppose we chose a set of deletion indices D such that after deletions, the final array has every element (row) in lexicographic order.

For clarity, A[0] is in lexicographic order (ie. A[0][0] <= A[0][1] <= ... <= A[0][A[0].length - 1]), A[1] is in lexicographic order (ie. A[1][0] <= A[1][1] <= ... <= A[1][A[1].length - 1]), and so on.

Return the minimum possible value of D.length.

 

Example 1:

Input: ["babca","bbazb"]
Output: 3
Explanation: After deleting columns 0, 1, and 4, the final array is A = ["bc", "az"].
Both these rows are individually in lexicographic order (ie. A[0][0] <= A[0][1] and A[1][0] <= A[1][1]).
Note that A[0] > A[1] - the array A isn't necessarily in lexicographic order.
Example 2:

Input: ["edcba"]
Output: 4
Explanation: If we delete less than 4 columns, the only row won't be lexicographically sorted.
Example 3:

Input: ["ghi","def","abc"]
Output: 0
Explanation: All rows are already lexicographically sorted.
 

Note:

1 <= A.length <= 100
1 <= A[i].length <= 100

"""

"""
This is a n^2 dp solution. This follows the idea of increasing subsequence.
inaddition to all previuos elements less than current element. .we also make the check for the all the words
and keep track of the maximum increasing subsequence..
if we have 4 maximum increasing subsequence.. we need to delete len(A[0]) - maxCount items

"""
class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        m = len(A)
        n = len(A[0])
        maxCount = [1 for i in range(0,n)]
        for j in range (1,n):
            for i in range(j):
                if all(A[k][i] <= A[k][j] for k in range(len(A))):
                    maxCount[j] = max(maxCount[j], maxCount[i]+1)
        return n- max(maxCount)
