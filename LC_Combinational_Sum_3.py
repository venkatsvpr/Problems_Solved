"""
216. Combination Sum III
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""
class Solution(object):
    """
    Approach:
    =========
    Add element to arraylist if it fits.. and call recruisively.. do a depth based search.
    Do a depth first based search...
    1) loop through all integers from 1 to 9, if arraylist is empty or Arraylist[-1]+1 to 9:
    2) if (i<n) add that to the arraylist and call for n = n-i and k = k-1
    3) When k is zero. n is zero add the arraylist to answer.

    n = 7 and k=3

    1-->2-->3 notpossible
    1-->2-->4 -- add to answer
    1-->2-->5 break
    1-->3
    1-->4
    1-->5
    1-->6
    """
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def rec_traverse (ArrayList, n , k, Ans):
            # If a n value run
            if (n == -1):
                return
            if (k == 0) and (n == 0):
                Ans.append(list(ArrayList))
            for i in range(ArrayList[-1]+1,10):
                if (i <= n):
                    Alist = list(ArrayList)
                    Alist.append(i)
                    rec_traverse(tuple(Alist),n-i,k-1,Ans)
            return
        Ans = []
        for i in range(1,9):
            if (i < n):
                Alist = []
                Alist.append(i)
                rec_traverse(tuple(Alist),n-i, k-1,Ans)
        return (Ans)
mysol = Solution()
print (mysol.combinationSum3(2,18))
print (mysol.combinationSum3(3,9))
print (mysol.combinationSum3(3,7))
