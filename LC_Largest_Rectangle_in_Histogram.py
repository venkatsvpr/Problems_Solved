"""
84. Largest Rectangle in Histogram
===================================
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].




The largest rectangle is shown in the shaded area, which has area = 10 unit.



Example:

Input: [2,1,5,6,2,3]
Output: 10


Have a stack to track the history of positions, first the stack is empty
Add a  0 to the height for easy processing.
Keep track of positions in the increasing order of height... go through heights one by one.. if we get a low height..
pop all the big ones out of the stack. calculate the area at every point in time... if it is greater than max area store it
At the end we will have the answer in max.

"""
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack = []
        ans = 0
        for i in range(len(heights)):
            while (len(stack)) and (heights[i] < heights[stack[-1]]):
                height = heights[stack.pop()]
                if (len(stack) == 0):
                    width = i
                else:
                    width = i - stack[-1] - 1
                ans = max(ans, height*width)
            stack.append(i)
        heights.pop(0)
        return ans
