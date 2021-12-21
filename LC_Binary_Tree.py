"""
704. Binary Search

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def rec(nums, start, end, target):
            mid = (start + end) / 2
            if start > end or end < start:
                return -1
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                return rec(nums, mid+1, end, target)
            if nums[mid] > target:
                return rec (nums, start, mid-1, target)
        return rec(nums, 0, len(nums)-1 ,target)
        
        
