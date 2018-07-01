"""
647. Palindromic Substrings

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Note:

   The input string length won't exceed 1000.

"""
class Solution(object):
    def countSubstrings(self, S):
        def ispalindrome (left,right,S):
            count = 0
            while (S[left] == S[right]):
                count += 1
                left -= 1
                right += 1
                if (left < 0):
                    break
                if (right > len(S)-1):
                    break
            return count

        N = len(S)
        ans = 0
        for item in range(len(S)):
            ans += ispalindrome(item, item, S)
        for item in range(len(S)-1):
            ans += ispalindrome(item, item+1, S)
        return ans
mysol = Solution()
mysol.countSubstrings("hellomadam")
