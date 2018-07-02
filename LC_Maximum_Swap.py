"""
670. Maximum Swap

Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
Note:
The given number is in the range [0, 108]
"""
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        lnum = list(str(num))
        for index,num in enumerate(lnum):
            if (index == len(lnum)-1):
                continue
            if (lnum[index] < lnum[index+1]):
                max_idx = index+1
                for idx in range(index+2,len(lnum)):
                    if (lnum[idx] >= lnum[max_idx]):
                        max_idx = idx
                for idx in range(0,index+1):
                    if (lnum[idx] < lnum[max_idx]):
                        lnum[idx],lnum[max_idx] = lnum[max_idx],lnum[idx]
                        return int("".join(lnum))
            else:
                continue;
        return int("".join(lnum))
mysol = Solution()
print (mysol.maximumSwap(9973))
print (mysol.maximumSwap(1329))
