"""347. Top K Frequent Elements

Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

import collections
from collections import Counter
"""
Count the number of items in the array given.
Use that and insert those elements into a priority queue


Approach2:
Use Bucket sort
find the frequency.
use frequency and insert into another hmap
then start from max number and decrement down and pick k elements

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        Ans  = []
        c = Counter(nums)
        keydict = collections.defaultdict(list)
        for key in c:
            keydict[c[key]].append(key)
        count = len(nums)

        while (count and (k>0)):
            if (count in keydict):
                k  -= len(keydict[count])
                for element in keydict[count]:
                    Ans.append(element)
                keydict[count] = []
            count -=1

        return Ans

import collections
from collections import Counter
"""
Count the number of items in the array given.
Use that and insert those elements into a priority queue


Approach2:
Use Bucket sort
"""
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        Ans  = []
        c = Counter(nums)
        keydict = collections.defaultdict(list)
        for key in c:
            keydict[c[key]].append(key)
        count = len(nums)
        while (count and (k>0)):
            if (count in keydict):
                k  -= len(keydict[count])
                for element in keydict[count]:
                    Ans.append(element)
                keydict[count] = []
            count -=1
        return Ans
