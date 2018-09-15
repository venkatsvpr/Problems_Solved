"""

301. Remove Invalid Parentheses

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
"""
"""
Approach:
Take a string frm queue.. check if it is valid... if it is valid.. add it to answer..
just see if anyone else in the queueis valid and add them to answer aswell.
<< This is veryimportatnt:: If there is a valid arrangment ... if we delete one more.. there will not be a valid string...
There could be potential ones after deleting two chracters.. but we already have the ones with max length >>>>

if the string doesnt have a valid ..
take every chracter out and add it to queue..
keep doing this.

We are dleeteing chracter by charater in all possible ways till we find a valid arrangement

Keep track of the element added to the queue and dont add it again.
"""
class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValid (s):
            count = 0
            for ch in s:
                if (ch == "("):
                    count += 1
                elif (ch == ")"):
                    count -= 1
                if (count < 0):
                    return False
            if (count > 0):
                return False
            return True

        Visited = dict()
        boolFound = False
        Queue = [s]
        Ans = []
        while (len(Queue)):
            NextQueue = []
            s = Queue.pop(0)
            if (isValid(s)):
                Ans.append(s)
                boolFound = True
                continue;
            for i in range(len(s)):
                if (s[i] != "(") and (s[i] != ")"):
                    continue;
                # Modified string
                toAdd = ""
                if (i == 0):
                    toAdd += s[1:]
                else:
                    toAdd += s[:i]+s[i+1:]
                if (toAdd in Visited):
                    continue;
                else:
                    Visited[toAdd] = True
                # If it is valid... set a bit to know that we have found the answer
                # and dont modify strings further
                if (isValid(toAdd)):
                    boolFound = True
                    Ans.append(toAdd)
                else:
                    NextQueue.append(toAdd)
            if (boolFound == False):
                Queue += NextQueue
        if (len(Ans) == 0):
            return [""]
        return list(set(Ans))
