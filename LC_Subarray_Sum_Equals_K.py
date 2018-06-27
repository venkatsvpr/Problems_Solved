"""
560. Subarray Sum Equals K
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        running = dict()
        rsum = 0
        running[0] = 1
        count = 0
        for num in nums:
            rsum += num
            if (rsum - k ) in running:
                count += running[rsum-k]
            if (rsum in running):
                running[rsum] += 1
            else:
                running[rsum] = 1
        return count

mysol = Solution()
print (mysol.subarrySum([1,1,1],2))
