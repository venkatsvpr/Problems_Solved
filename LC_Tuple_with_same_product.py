"""
1726. Tuple with Same Product
Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d.

 

Example 1:

Input: nums = [2,3,4,6]
Output: 8
Explanation: There are 8 valid tuples:
(2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
(3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
Example 2:

Input: nums = [1,2,4,5,10]
Output: 16
Explanation: There are 16 valid tuples:
(1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
(2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
(2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,5,4)
(4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 104
All elements in nums are distinct.
"""
import collections
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # Compute all products
        prod = collections.Counter()
        for idx1 in range(0, len(nums)):
            for idx2 in range(idx1+1, len(nums)):
                prod[nums[idx1] * nums[idx2]] += 1
        count = 0 
        for key in prod:
            # there is only effort to pick the first 2, rest are automatic.
            # We do nC2 = n! / (n-r)! * r! = n * n-1 / 2!
            count += prod[key] * (prod[key] - 1)/2
        # Since there are 4 numbers, each can be represented in 4! ways 4*2= 8
        return int(count * 8)