"""
https://leetcode.com/problems/majority-element/description/

Initialize a counter to zero
for all numbers:
    if counter is zero. store the number as answer.
    if number equal to answer incremenet the counter.
    if number not equal decremenent the counter
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0;
        answer = -1
        for num in nums:
            if count == 0:
                answer = num
            if  (answer == num):
                count = count + 1
            else:
                count = count -1
        return answer
