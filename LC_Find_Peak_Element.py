# Find Peak Element
# https://leetcode.com/problems/find-peak-element/
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        left = 0
        right = len(nums) -1

        while(left <right):
            mid = (left+right)/2
            """
            Check if middle element is bigger than its next number
            If (big) search the left side.
            else search the right side
            """
            if (nums[mid] > nums[mid+1]):
                right = mid
            else:
                left = mid+1
        return left
