"""
163. Missing Ranges

Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

Example:

Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]
"""

"""
Approach:

store the prev number..
initial value of prev =lower-1
fro every number... try insert with  prev and num.. actual insert will happen between prev+1 and num-1
"""
class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        def insert (start , end, Ans):
            if (end-start == 1):
                return
            if (start+1 == end-1):
                Ans.append(str(start+1))
            else:
                Ans.append(str(start+1)+"->"+str(end-1))
            return

        if (0 == len(nums)):
            if (lower == upper):
                return [str(lower)]
            return [str(lower)+"->"+str(upper)]

        Ans = []
        # this has to be set to lower-1
        prev = lower-1
        for num in nums:
            if (prev != num):
                insert (prev, num, Ans)
            prev = num
        insert (prev, upper+1, Ans)
        return (Ans)
