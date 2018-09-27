"""

245. Shortest Word Distance III

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “makes”, word2 = “coding”
Output: 1
Input: word1 = "makes", word2 = "makes"
Output: 3
Note:
You may assume word1 and word2 are both in the list.
"""

import collections
class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # Use this to find the min difference between two points on a list
        def findmin (lt):
            minVal = float('inf')
            prev = None
            for num in lt:
                if (prev == None):
                    prev = num
                    continue;
                minVal = min (minVal, num-prev)
                prev = num
            return minVal

        # Use this to find the min dfiference between two points each from alist
        def findShortest (lt1, lt2):
            newlt1 = sorted(lt1[:])
            newlt2 = sorted(lt2[:])

            it1 = newlt1.pop(0)
            it2 = newlt2.pop(0)
            minval = float(abs(it1-it2))

            while (len(newlt1) or len(newlt2)):
                if (it1 < it2):
                    minval = min (minval, abs(it2-it1))
                    if (len(newlt1) == 0):
                        break
                    it1 = newlt1.pop(0)
                else:
                    minval = min (minval, abs(it1-it2))
                    if (len(newlt2) == 0):
                        break
                    it2 = newlt2.pop(0)

            minval = min (minval, abs(it1-it2))
            return minval

        # push the word as key and the idx into a collection
        wordSymbol = collections.defaultdict(list)
        for index,word in enumerate(words):
            wordSymbol[word].append(index)
        # If both words are same find min difference between two elements in a list
        if (word1 == word2):
            return int(findmin(wordSymbol[word1]))
        # if both are different find min different btween two elements in different lists
        return int(findShortest(wordSymbol[word1], wordSymbol[word2]))
        
