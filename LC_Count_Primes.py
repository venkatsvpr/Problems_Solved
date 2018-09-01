"""
204. Count Primes


Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        not_prime = [False] * n
        count = 0
        for i in range(2, n):
            if not not_prime[i]:
                count += 1
                j = 2
                while (i*j < n):
                    not_prime[i*j] = True
                    j += 1
        return count
