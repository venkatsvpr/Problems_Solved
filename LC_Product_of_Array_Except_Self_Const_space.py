"""
238. Product of Array Except Self
==================================
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

"""
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        The logic is simple. Find the product of the left side..
        Find the product of the right side and multiple  both
        """

        output = []
        p = 1

        #Find left multiplication results
        output.append(1)
        for i in range(len(nums)-1):
            p *= nums[i]
            output.append(p)

        right = []
        p = 1
        i = len(nums)-1

        #Multiple each and every element with the right mulitplication results.
        while (i >= 1):
            p *= nums[i]
            output[i-1] = output[i-1]*p
            i -= 1

        return (output)
