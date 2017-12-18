# Solution to License Key Formatting Problem
# https://leetcode.com/problems/license-key-formatting/description/
class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.upper().replace('-','');
        size =len(S)
        s1 = K if size%K == 0 else size %K
        res = S[:s1]
        while (s1<size):
            res += '-'+S[s1:s1+K]
            s1 += K
        return res
   

