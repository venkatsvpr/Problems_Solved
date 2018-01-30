"""
https://leetcode.com/problems/permutations-ii/description/

This is similar to 
https://leetcode.com/problems/permutations/description/
With an extra check.. store a list of previous visited.. and skip if it comes again .

Similar to the previous problem. store the result and we are done
"""
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def rec_permute (a, l, r):
            global Answer;
            if (l == r):
                Answer.append(list(a))
            else:
                proc = []
                for i in range(l,r+1):
                    if (a[i] in proc):
                        continue;
                    proc.append(a[i])
                    a[i],a[l] = a[l],a[i]
                    rec_permute (a, l+1,r)
                    a[i],a[l] = a[l],a[i]
        global Answer
        Answer =[]
        if (len(nums) != 0):
            rec_permute (nums, 0, len(nums)-1)
        return (Answer)  
