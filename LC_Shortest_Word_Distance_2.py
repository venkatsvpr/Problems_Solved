"""

244. Shortest Word Distance II

Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list. Your method will be called repeatedly many times with different parameters.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
"""

"""
Same as shortest word distance 3..
add caching since this can be called multiple times
"""
import collections
class WordDistance(object):
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.cache = dict()
        self.wordSymbol = collections.defaultdict(list)
        for index,word in enumerate(words):
            self.wordSymbol[word].append(index)

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
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
            return int(minval)

        if (word1,word2) in self.cache:
            return self.cache[(word1,word2)]
        self.cache[(word1,word2)] = findShortest(self.wordSymbol[word1], self.wordSymbol[word2])
        return self.cache[(word1,word2)]



# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
