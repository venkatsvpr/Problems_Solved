""" 
Regular Expression Matching
https://leetcode.com/problems/regular-expression-matching/description/
"""
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        w = len(p)
        h = len(s) 
        """ Create a Matrix for storing the True/False Values. Actually can be done with an two 1d array itself"""
        Matrix = [[False for x in range(w+1)] for y in range(h+1)] 
      
        """ Initialize the initial value as True"""
        Matrix[0][0] = True
       
        """ When the pattern is `a*` we can say that it is a match for zero input """
        for i in range(0,len(p)+1):
            if (i == 0):
                continue
                
            if (p[i-1] == "*"):
                Matrix[0][i] = Matrix[0][i-2];
        
        """ Run a loop for the len(s) and len(p) and fill the table """
        for i in range(0,len(s)+1):
            for j in range(0,len(p)+1):
                if (i == 0):
                    continue;
                    
                if (j == 0):
                    continue;
                """ If the character is same (or) dot , Mark it with the (i-1,j-1) value """               
                if (p[j-1] == s[i-1] or p[j-1]== "."):
                    Matrix[i][j] =  Matrix[i-1][j-1]
                """ If the pattern is *, take the [i][j-2] value """
                elif (p[j-1] == "*"):
                    Matrix[i][j] = Matrix[i][j-2]
                    """ If the the pattern matches with the previous s[i-1] take the i-1,j value """
                    if (p[j-2] == "." or s[i-1] == p[j-2]):
                        if (Matrix[i-1][j] == True):
                            Matrix[i][j] = True;
            
        return (Matrix[h][w])
        
        
