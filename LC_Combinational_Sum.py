"""
39. Combination Sum

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""

"""
Approach:
=========
Do a depth based search, recursively.
-> Go down if target is positive.. If expected is zero save the Answer.
-> If expected is negative return there.
At ever point.. loop through all the candidates.. which are equal or greater than..
This is done so as to avoid duplicates.
"""
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def rec_traverse (stack, expected, candidates, Ans):
            # since all numbers are positive.. we cant make an negative expected number
            if (expected < -1):
                return
            if (expected == 0):
                Ans.append(stack)
            for item in candidates:
                # So as to avoid duplicate pairs
                if (stack and stack[-1] < item):
                    continue;
                # If there is still scope recurse again
                if (expected - item >= 0):
                    rec_traverse(stack +[item] , expected-item, candidates, Ans)
        Ans = []
        rec_traverse ([], target, candidates, Ans)
        return (Ans)
