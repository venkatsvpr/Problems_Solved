"""
1020. Partition Array Into Three Parts With Equal Sum
Given an array A of integers, return true if and only if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i+1 < j with (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])

 

Example 1:

Input: [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
Example 2:

Input: [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false
Example 3:

Input: [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
 

Note:

3 <= A.length <= 50000
-10000 <= A[i] <= 10000
"""

"""
If we are splitting into three ranges the three ranges will be of sum.. totalSum/3
Keep track of the running Sum.. when we hit totalSum/3 we have to start looking for the next range..  when we find already two ranges. the rest should be sum totalSum/3
"""
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        rsum = 0
        totalSum = sum(A)
        count = 0
        i = 0
        while i < len(A):
            rsum += A[i]
            if (rsum == totalSum/3):
                rsum = 0
                count += 1
                if (count == 2):
                    if (totalSum/3 == sum(A[i+1:])):
                        return True
                    else:
                        return False
            i += 1
        if (count < 2):
            return False
        return True
