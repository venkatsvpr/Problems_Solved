# Generate Paranthesis
# https://leetcode.com/problems/generate-parentheses/description/
class Solution(object):
    def generateParenthesis(self, N):
        ans=[]
        def dfs (S ='',open = 0 , close =0):
            if (N == close):
                ans.append(S)
                return
            if (open > close):
                dfs (S+')', open, close+1)
            if (open < N):
                dfs (S+'(', open+1, close)

        
        dfs ()
        return ans
