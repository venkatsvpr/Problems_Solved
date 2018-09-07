"""
399. Evaluate Division


Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.

"""

"""
Store the Node next node in a default dict(list)
store the path cost between two nodes in a dictionary

if any of the source or destioantion is not there in next.. then return -1
if we have any a,b in dictionary return that as anaswer
if a==b and we know a... return  1 as answer
else use backtrack and recurison in funciton find


find:
this is simple backtracker.
looks at the next and calls it for all the next.. stores the current node in past so that it is not visited again.
if the next returns true.. take the value and the multiple it with the current value and push it up.
if the next returns false..  return false and zero up

"""
import collections
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        def find (up, down, Next, d, Past):
            for item in Next[up]:
                # Ensure we dont indefinetely loop
                if (item in Past):
                    continue
                if (item == down):
                    return [True, d[(up,item)]]
                # Add the element to the set for backtracking
                Past.add(up)
                [retval, temp] = find (item, down, Next, d, Past)
                # rmeove the element from the set
                Past.remove(up)
                # if the ret value is true.. multiplly current value and push up
                if (retval == True):
                    return [True, (temp * d[(up,item)])]
            return [False, -1]

        d = dict()
        Next = collections.defaultdict(list)
        # populate the neighbours and a/b value also b/a value
        for [up, down],value in zip(equations,values):
            d[(up,down)] = value
            d[(down,up)] = 1/value
            Next[up].append(down)
            Next[down].append(up)

        Ans = []
        Past = set()
        for [up,down] in queries:
            if (up not in Next) or (down not in Next):
                Ans.append(float(-1))
            elif ((up,down) in d):
                Ans.append(d[(up,down)])
            elif (up == down):
                Ans.append(float(1))
            else:
                retval = find(up,down,Next,d,Past)
                Ans.append(float(retval[1]))
        return Ans
