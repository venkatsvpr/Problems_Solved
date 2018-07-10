"""
40. Combination Sum II
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""
"""
Approach:
1) Take a number and do depth first search.. Do backtrack aswell
2) target is negative.. then cant proceed.
3) if target is zero. Append the past to Answer
4) ensure that smaller numbers are not visited... so as to ensure unique numbers.
"""
import collections
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def rec_sum (past, target, clist, ccount, Ans):
            if (target < 0):
                return
            if (target == 0):
                Ans.append(past)
                return
            for item in clist:
                if past and past[-1] < item:
                    continue;
                if (ccount[item] > 0):
                    ccount[item] -= 1
                    rec_sum ( past +[item], target-item, clist, ccount, Ans)
                    ccount[item] += 1
        ccount = collections.Counter(candidates)
        Ans = []
        rec_sum ([],target,set(candidates),ccount,Ans)
        return (Ans)    
