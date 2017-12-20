# Repeated String Matching
# https://leetcode.com/problems/repeated-string-match/description/
class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if (len(A) == len(B)):
            if (A in B):
                return 1
            else:
                str = "" 
                count = int((len(A)/len(B))+2);
                max_count =  int(count);
                while (count!=0):
                    str += A
                    if (B in str):
                        return max_count  -int(count)+1;
                    count -= 1;       
        elif (len(A) > len(B)):
            str = "" 
            count = int((len(A)/len(B))+2);
            max_count =  int(count);
            while (count!=0):
                str += A
                if (B in str):
                    return max_count  -int(count)+1;
                count -= 1;       
        elif (len (B) > len(A)):
            str = "" 
            count = int((len(B)/len(A))+2);
            max_count =  int(count);
            while (count!=0):
                str += A
                if (B in str):
                    return max_count  -int(count)+1;
                count -= 1;
        return -1;      
        
        
