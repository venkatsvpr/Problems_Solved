"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

"""

"""
Add elements to the stack till it is full..
Once it is full.. pop elemnts from the end.. and use the next number as x.


"""
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        stack = []
        x = 1
        res = []
        while (True):
            # Breaking conidition... x >n and there are no more elements to be processed
            if (x > n) and (len(stack) == 0):
                break
            # if length of stack == k or x > n
            if (len(stack) == k) or (x > n):
                if (len(stack) == k):
                    res.append(stack[:])
                x = stack.pop() + 1
            else:
                stack.append(x)
                x += 1
        return res
