"""
84. Largest Rectangle in Histogram
===================================
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].




The largest rectangle is shown in the shaded area, which has area = 10 unit.



Example:

Input: [2,1,5,6,2,3]
Output: 10

"""
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # Add a marker to the heights array to denote that it is ended
        heights.append(0)
        # populate the stack with -1
        stack = [-1]
        ans = 0
        for i in range(len(heights)):
            # pop all the element's index from stack whose height is greather than the ith height.
            # find area in all the cases.
            while(heights[i] < heights[stack[-1]]):
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                ans = max(ans, height*width)
            # append the index to the stack.
            stack.append(i)
        heights.pop(0)
        return ans
