"""
Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.

 

Example 1:

Input: n = 12
Output: 21
Example 2:

Input: n = 21
Output: -1
 

Constraints:

1 <= n <= 231 - 1
"""
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        a = list(str(n))
            
        ## First point that is less than the next point
        i = len(a)-2
        while i >=0 and a[i]>= a[i+1]:
            i -= 1
        
        # If we are unable to find a point errorr out
        if i < 0:
            return -1
        
        # find the replacement for this point.. Come from right and find the one that is at least greater than the point
        j = len(a)-1
        while (j >= 0 and a[j] <= a[i]):
            j -= 1
        
        a[i],a[j] = a[j],a[i]
        r = a[:i+1]  + a[len(a)-1:i: -1]

        res = int(''.join(r))
        if res <= 2**31-1:
            return res
        return -1
        