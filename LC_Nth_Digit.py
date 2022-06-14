"""

400. Nth Digit


Given an integer n, return the nth digit of the infinite integer sequence [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...].

 

Example 1:

Input: n = 3
Output: 3
Example 2:

Input: n = 11
Output: 0
Explanation: The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
 

Constraints:

1 <= n <= 231 - 1
"""
class Solution:
    def findNthDigit(self, n: int) -> int:
        # Logic to cout the number of digits
        def find(check):
            start = 1
            digits = 0
            times = 1
            while (True):
                if check >= (start * 10):
                    digits +=  times * (((start * 10) -1) - start + 1)
                else:
                    digits +=  times * ((check - start + 1))
                    break
                times += 1
                start = start * 10
            return digits
        
        # Binary searcht for the digit
        def findDigit():
            left,right = 1, n
            while (left < right):
                mid = left + (right - left)//2
                # If the digit is in the current mid
                if find(mid) >=n and find(mid-1) < n:
                    return mid
                elif find(mid) < n:
                    left = mid + 1
                elif find(mid) > n:
                    right = mid - 1
            return left
        
        digit = findDigit()
        strDigit = str(digit)   
        offset = n - find(digit-1)
        return strDigit[offset-1]