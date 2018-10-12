"""
119. Pascal's Triangle II

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
"""
"""
Similar to old problem.
instead of emitting all the level send only the answer level alone

At every level, we perfrom addition of the consecutive numbers and progpagate it down
            1
        1       1
    1       2       1
1       3       3       1

So at every level. we kind of preserve the first and last number of the previous level
and perform a sum of the conssecitve numbers and get the middle elemetns.
"""
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # Return a list which is a sum of consecutive numbers.
        def getNext (Lt):
            tAns = []
            for i in range(len(Lt)-1):
                tAns.append(Lt[i]+ Lt[i+1])
            return tAns
        if (rowIndex == 0):
            return [1]
        Ans = [1]
        for i in range(rowIndex):
            if (1 == len(Ans)):
                Ans = [Ans[0], Ans[-1]]
            else:
                Ans = [Ans[0]] + getNext(Ans) + [Ans[-1]]
        return Ans
