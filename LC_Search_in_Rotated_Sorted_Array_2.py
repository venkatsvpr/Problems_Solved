"""
81. Search in Rotated Sorted Array II

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?

Approach: 
A half could be sorted. If our number is sorted.. binary search in that half
check both halfs for sortenes.. if not possible.. search on both halfs.
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        def binarySearch (start, end, nums, target):
            if (start > end) or(end > len(nums)-1):
                return False
            mid = (start + end)/2
            if (nums[mid] == target) or (nums[start] == target) or (nums[end] == target):
                return True
            # Check if left half is sorted and check if our data is in it
            if (nums[start] < nums[mid]):
                if (nums[start] <= target <= nums[mid]):
                    return binarySearch (start, mid-1, nums, target)
                elif (target > nums[mid]):
                    return binarySearch (mid+1, end, nums, target)
            # Check if right data is sorted and check our data is in it
            if (nums[mid] < nums[end]):
                if (nums[mid] <= target <= nums[end]):
                    return binarySearch (mid+1, end, nums,target)
                elif (target < nums[mid]):
                    return binarySearch (start, mid-1, nums,target)
            # search both sides. if not possible.
            return (binarySearch(start, mid-1, nums, target) or binarySearch(mid+1, end, nums, target))
        return binarySearch (0, len(nums)-1, nums, target)
