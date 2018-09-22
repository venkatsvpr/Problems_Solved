"""
35. Search Insert Position
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0

Approach :
Try doing binary search . see if low, mid, high equals to the target
if target is greater than high.. return high + 1
if target is less than low.. return low
if num at mid is greater than target
    high = mid-1
if num at mid is less than target
    low = mid+1
else reduce the high
or increase the low
"""
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low =  0
        high = len(nums)-1
        while (low < high):
            mid = (low+high)/2
            StartMidEnd = [low, mid, high]
            for pt in StartMidEnd:
                if (nums[pt] == target):
                    return pt
            if (nums[high] < target):
                return high+1
            if (nums[low] > target):
                return low
            elif (nums[mid] > target):
                high = mid-1
            elif (nums[mid] < target):
                low = mid+1
        if (nums[low] >= target):
            return low
        if (nums[low] < target):
            return low+1
