"""
219. Contins Duplicate II

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = dict()
        for index,num in enumerate(nums):
            if (num in d) and (abs(index -d[num]) <=k):
                return True
            d[num] = index
        return False
mysol = Solution()
print (mysol.containsNearbyDuplicate([1,2,3,1],3))
print (mysol.containsNearbyDuplicate([1,0,1,1],1))
print (mysol.containsNearbyDuplicate([1,2,3,1,2,3],2))
