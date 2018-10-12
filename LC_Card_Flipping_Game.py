"""
822. Card Flipping Game

On a table are N cards, with a positive integer printed on the front and back of each card (possibly different).

We flip any number of cards, and after we choose one card.

If the number X on the back of the chosen card is not on the front of any card, then this number X is good.

What is the smallest number that is good?  If no number is good, output 0.

Here, fronts[i] and backs[i] represent the number on the front and back of card i.

A flip swaps the front and back numbers, so the value on the front is now on the back and vice versa.

Example:

Input: fronts = [1,2,4,4,7], backs = [1,3,4,1,3]
Output: 2
Explanation: If we flip the second card, the fronts are [1,3,4,4,7] and the backs are [1,2,4,1,3].
We choose the second card, which has number 2 on the back, and it isn't on the front of any card, so 2 is good.


Note:

1 <= fronts.length == backs.length <= 1000.
1 <= fronts[i] <= 2000.
1 <= backs[i] <= 2000.


"""

"""
For an index i, if front[i] == back[i] that can never be the answer.
so add it to same set.
we can rotate cards any number of times.. so pick the minimum card in front and back
which is not in the same set.
if we are not able to find.. the answer should be 0
"""
class Solution(object):
    def flipgame(self, fronts, backs):
        same = set()
        for i,front in enumerate(fronts):
            if (front == backs[i]):
                same.add(front)
        minAns = float('inf')
        for item in fronts+backs:
            if (item not in same):
                minAns = min(minAns, item)
        if (minAns == float('inf')):
            return 0
        return minAns
