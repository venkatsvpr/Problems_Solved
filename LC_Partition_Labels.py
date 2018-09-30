"""
763. Partition Labels


A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
Note:

S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.

"""

"""
Store the last seen idx for every character.
loop through every character..
set the maxNow = lastseenidx[ch]
keep see all characters till that point.. if see a idx which is more update maxNow.
when we see an idx.. matching maxNow ...  add answer to i-start+1.. set the new start to i+1
"""
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        # keep track of the characters seen
        lastSeen = dict()
        for idx,ch in enumerate(S):
            lastSeen[ch] = idx
        maxNow = 0
        start = 0
        Ans = []
        for i in range(len(S)):
            # update the max value
            maxNow = max(maxNow, lastSeen[S[i]])
            # when i reaches max.. store the answer.. and set the new start to start+1
            if (i == maxNow):
                Ans.append(i-start+1)
                start = i+1
        return (Ans)
                
