"""
403. Frog Jump

A frog is crossing a river. The river is divided into x units and at each unit there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog is able to cross the river by landing on the last stone. Initially, the frog is on the first stone and assume the first jump must be 1 unit.

If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units. Note that the frog can only jump in the forward direction.

Note:

The number of stones is ≥ 2 and is < 1,100.
Each stone's position will be a non-negative integer < 231.
The first stone's position is always 0.
Example 1:

[0,1,3,5,6,8,12,17]

There are a total of 8 stones.
The first stone at the 0th unit, second stone at the 1st unit,
third stone at the 3rd unit, and so on...
The last stone at the 17th unit.

Return true. The frog can jump to the last stone by jumping
1 unit to the 2nd stone, then 2 units to the 3rd stone, then
2 units to the 4th stone, then 3 units to the 6th stone,
4 units to the 7th stone, and 5 units to the 8th stone.
Example 2:

[0,1,2,3,4,8,9,11]

Return false. There is no way to jump to the last stone as
the gap between the 5th and 6th stone is too large.
"""


class Solution:
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        def rec_jump(i,jump):
            # Memoization
            if (i,jump) in memo:
                return memo[(i,jump)]
            # If the stone is not there return false
            if (i+jump not in st):
                return False
            # If we have reached the end stone return true
            elif (i+jump == stones[-1]):
                #print ("returning ture",i,jump)
                return True
            # add the previous jump to the i
            i = i + jump

            # from current i , see all possible jumps and see if in
            # any one of the ways we will hit the end
            if (jump > 1):
                if (rec_jump(i,jump) or rec_jump(i,jump-1) or rec_jump(i,jump+1)):
                    memo[(i-jump,jump)] = True
                    return True
            elif (jump == 1):
                if (rec_jump(i,jump) or rec_jump(i,jump+1)):
                    memo[(i-jump,jump)] = True
                    return True
            else:
                if (True == rec_jump(i,jump+1)):
                    memo[(i-jump,jump)] = True
                    return True
            # Memoize the result
            memo[(i-jump,jump)] = False
            return False

        # Dictionaries for memoization
        st = dict()
        memo = dict()

        # Store the stone position in a hash for O(1) lookup
        for stone in stones:
            st[stone] = True

        return (rec_jump(0,0))

mysol = Solution()
stones_array = [0,1,3,5,6,8,12,17]
print (mysol.canCross(stones_array))
stones_array = [0,1,2,3,4,8,9,11]
print (mysol.canCross(stones_array))
