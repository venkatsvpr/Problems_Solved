"""

846. Hand of Straights


Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

 

Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
Example 2:

Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation: Alice's hand can not be rearranged into groups of 4.

 

Constraints:

1 <= hand.length <= 104
0 <= hand[i] <= 109
1 <= groupSize <= hand.length
 

Note: This question is the same as 1296: https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

"""
import collections
class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        # push this to a counter
        c = collections.Counter(hand)
        
        # find the maximum value
        maxVal = hand[0]
        for h in hand[1:]:
            maxVal = max(maxVal, h)
            
        if maxVal == 0:
            return False
        # Loop from that value and try to pick groupSize which are nearby
        while (maxVal):
            backup = maxVal
            if c[maxVal] == 0:
                maxVal -= 1
                continue
            for i in range(groupSize):
                if c[maxVal] > 0 :
                    c[maxVal] -= 1
                    maxVal -= 1
                else:
                    return False
            maxVal = backup
        return True
        