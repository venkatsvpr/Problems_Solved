"""
581. Shortest Unsorted Continuous Subarray
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
"""

"""
Approach:
- Find point of anamoly from the left, after that find the min element
- find point of anamoly from the right, after that find the max element
- find the L value.. position where min element can be inserted, this will mark the first  thing to sort
- find the R value.. position where max element can be inserted, this will mark the last thing we need to sort
- That is the range we have to stort.
"""
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minElement = float('inf')
        maxElement = float('-inf')
        flag = False
        for i in range((len(nums)-1)):
            if (nums[i] > nums[i+1]):
                flag = True
            if (flag):
                minElement = min(minElement, nums[i+1])

        flag = False
        for i in range (len(nums)-2,-1,-1):
            if (nums[i]  > nums[i+1]):
                #print ("flat true for ",i,maxElement)
                flag = True
            if (flag):
                #print (" setting max as ",nums[i])
                maxElement = max(maxElement, nums[i])

        for l in range(len(nums)):
            if (minElement < nums[l]):
                break;
        for r in range(len(nums)-1,0,-1):
            if (maxElement > nums[r]):
                break
        #print (minElement,maxElement,l,r)
        if (minElement == float('inf')) and (maxElement==float('-inf')):
            return 0
        if (r-l < 0):
            return len(nums)
        return r-l+1
        
