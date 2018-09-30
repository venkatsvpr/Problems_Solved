"""
60. Permutation Sequence

The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
"""

"""
Approach:
Lets take [1,2,3]
the permutations inorder are (1,2,3) (1,3,2) (2,1,3) (2,3,1)  (3,1,2)  (3,2,1)
we can see that the for ever number as the first there are (n-1)! combinations.

We are going to use this property and build the answer.
we first fix the first numberand keep on fixing other numbers. for the kth permutation sequence.

lets take N=3 and k =3
==> k = 2
decerement n by one in a loop
see if k / factorial(n) .. quotient wil give the idx of the potiion that we have to add to the answer.
the reminder will give us the future k with which we can work on.
once an index is added remove it from the list
"""
import math
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        numbers = [i for i in range(1,n+1)]
        idx = 0
        k -= 1
        Ans = ""
        while (n):
            n -= 1
            # Find the index that we are interested int
            idx = k / math.factorial(n)
            # Find the reminder for further transactions
            k  = k % math.factorial(n)
            # append the index to answer and remove it at every stage
            Ans +=  str(numbers[idx])
            numbers.remove(numbers[idx])
        return Ans
        
