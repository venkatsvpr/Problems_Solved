"""
https://leetcode.com/problems/permutations/description/
ABC - First Step Swap (a,a) (a,b) (a,c)
Fix the first number.. repeat the same for the second..  
Backtrack on each step.
Store the answer.

Logic:
https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
"""
Answer =[]
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def rec_permute (a, l, r):
            global Answer;
            if (l == r):
                Answer.append(list(a))
            else:
                for i in range(l,r+1):
                    a[i],a[l] = a[l],a[i]
                    rec_permute (a, l+1,r)
                    a[i],a[l] = a[l],a[i]
        global Answer
        Answer =[]
        if (len(nums) != 0):
            rec_permute (nums, 0, len(nums)-1)
        return (Answer)
