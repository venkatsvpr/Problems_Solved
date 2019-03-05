"""
1002. Find Common Characters

Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

 

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]
 

Note:

1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter
"""

class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        def freq(word):
            lt = [0 for i in range(26)]
            word = word.lower()
            for idx,ch in enumerate(word):
                lt[ord(ch)-ord("a")] += 1
            return lt
        freqWords = [freq(word) for word in A]
        for i in range(1,len(freqWords)):
            for j in range(26):
                freqWords[0][j] = min(freqWords[0][j],freqWords[i][j])
        Ans = []
        for idx,count in enumerate(freqWords[0]):
            if (count > 0):
                Ans += [str(chr(ord("a")+idx)) for i in range(count)]
        return (Ans)
