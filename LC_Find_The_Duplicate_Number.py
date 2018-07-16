"""
287. Find the Duplicate Number
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""
"""
Approach:
This is similar to finding the looping point on a linkedlist.
1) Have two pointers.. slow and fast.. when they meet there is  a loop. Note the point.
2) Start from first element and the loop point and increment both ..they will meet at the looping point.

"""
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = nums[0]
        fast = nums[0]
        while (True):
            #print (" looping ,",slow,fast)
            slow = nums[slow]
            fast = nums[nums[fast]]
            if (slow == fast):
                break;

        pt1 = nums[0]
        pt2 = fast
        while (pt1 != pt2):
            #print (" pt1 pt2 ",pt1,pt2)
            pt1 = nums[pt1]
            pt2 = nums[pt2]
        return pt1
