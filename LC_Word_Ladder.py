"""
127. Word Ladder

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""

"""
Add the beginword to the Queue.
get the size of the Queue and process the size in an inside loop.
Get the change every character by 'a' to 'z' and see if the element is in the wordlist.
If it is there add it to the Queue
if the destinationword is found. .return the level + 1 as answer.

keep doing this.. ultimately the word has ot be found.
if we are done with the queue.. reutrn -1
"""
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # Set for wordlist
        d = set()
        for word in wordList:
            d.add(word)
        # If endword is not in d, return 0
        if (endWord not in d):
            return 0

        # Start with beginWord in Queue
        Queue = [beginWord]
        # This is the level value.. do a level order traversal
        level = 0
        # Start with Queue
        while (len(Queue)):
            size = len(Queue)
            level += 1
            # Visit all the elements of size
            for i in range(size):
                # Pop elements from the Queue
                word = Queue.pop(0)
                # pick the word and change every character from 'a' to 'z'
                for j in range (len(word)):
                    for k in range(26):
                        newword = word[:j] + chr(ord('a')+k)+ word[j+1:]
                        # if we have found the endword return level+1
                        if (newword == endWord):
                            return level+1
                        # If the word is in d..remove it from d and add the word to Queue
                        if (newword in d):
                            d.remove(newword)
                            Queue.append(newword)
        # not found
        return 0
