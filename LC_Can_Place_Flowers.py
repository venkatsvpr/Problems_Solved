"""
https://leetcode.com/problems/can-place-flowers/description/
Keep a track of the previous and prev-previous element. If both are zero and current element is zero a flower can be placed at the previous position.
For the first and last we implicitly take that the previuos and next elements are zero.
"""
class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        possible_n = 0
        if not flowerbed:
            if n == 0:
                return True
            else:
                return False
        prev_element = 0
        curr_element = -1;
        for index in range(0,len(flowerbed)):
            if (index == 0):
                curr_element = flowerbed[index]
                continue
            if (flowerbed[index] == 0):
                if (prev_element==0 and curr_element == 0):
                    flowerbed[index-1] = 1
                    curr_element = 0;
                    prev_element = 1;
                    possible_n += 1
                    continue;
                    
            prev_element = curr_element
            curr_element = flowerbed[index]
        if (prev_element == 0 and curr_element == 0):
            possible_n += 1
        if (n <= possible_n):
            return True
        return False
