"""
665. Non-decreasing Array


Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
Note: The n belongs to [1, 10,000].
"""
""" Simple logic
Step 1:
Traverse from left to right.. there should be only one position where we find a high to low conversion.
if we find second it is not possible
Step 2:
Traverse from right to left... there should be only one position where we find a low to high conversion.
If we find second it is not possible.
Either of step 1 and step2 should be true.
"""
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        flag = False
        count = 0
        prev = nums[0]
        for i in range(1,len(nums)):
            if (nums[i] < prev):
                if (flag == True):
                    count = 1
                    break;
                flag = True
                continue;
            prev = nums[i]
        if (count == 0):
            return True
        flag = False
        prev = nums[len(nums)-1]
        count = 0
        for i in range(len(nums)-2, -1,-1):
            if (nums[i] > prev):
                if (flag == True):
                    count = 1
                    break;
                flag = True
                continue;
            prev = nums[i]
        if (count == 0):
            return True
        return False
        
