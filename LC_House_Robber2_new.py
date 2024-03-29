"""
213. House Robber II
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def bestrob(nums):
            print (nums)
            if ((nums is None) and (len(nums) == 0)):
                return 0
            now = prev = 0
            for n in nums:
                now,prev = max(now,prev+n) ,now
            return max(prev,now)
        if (len(nums) == 1):
            return nums[0]
        return max(bestrob(nums[1:]), bestrob(nums[:-1]))

class Solution:
    def rob(self, nums: List[int]) -> int:
        def houseRob(nums: List[int]) -> int:
        # at every level we have two options
        # with - current best + previous without best
        # without  - max(prev with best, prev without best)
        # final answer is max of both
            w = wo = 0
            for num in reversed(nums):
                w, wo = num + wo, max(w,wo)
            return max(w,wo)
        if len(nums) == 1:
            return nums[0]
        return max(houseRob(nums[1:]), houseRob(nums[:-1]))