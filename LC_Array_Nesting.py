"""
565. Array Nesting
A zero-indexed array A of length N contains all integers from 0 to N-1. Find and return the longest length of set S, where S[i] = {A[i], A[A[i]], A[A[A[i]]], ... } subjected to the rule below.

Suppose the first element in S starts with the selection of element A[i] of index = i, the next element in S should be A[A[i]], and then A[A[A[i]]]… By that analogy, we stop adding right before a duplicate element occurs in S.

Example 1:
Input: A = [5,4,0,3,1,6,2]
Output: 4
Explanation:
A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.

One of the longest S[K]:
S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}
Note:
N is an integer within the range [1, 20,000].
The elements of A are all distinct.
Each element of A is an integer within the range [0, N-1].
"""

class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hmap =dict()
        past = dict()
        # Insert the key as the index and the value as the value
        # into the hashmap
        for index,num in enumerate(nums):
            hmap[index] = num
        maxCount = 0

        # For key in hashmap
        for key in hmap:
            Count = 0
            # Dont go through the past keys again.
            if (key in past):
                continue;
            tovisit = []
            tovisit.append(key)
            # Traverse through the item which satisifies the property
            while ((tovisit) and (tovisit[0] not in past)):
                item = tovisit.pop()
                past[item] = True
                Count += 1
                tovisit.append(hmap[item])
            maxCount = max(Count, maxCount)
        return maxCount

mysol = Solution()
mysol.arrayNesting([5,4,0,3,1,6,2])
