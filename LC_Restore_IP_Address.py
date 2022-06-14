"""
93. Restore IP Addresses

A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

 

Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
Example 2:

Input: s = "0000"
Output: ["0.0.0.0"]
Example 3:

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
 

Constraints:

1 <= s.length <= 20
s consists of digits only.

"""
class Solution:
    def __init__(self):
        self.d = dict()
        self.Ans = list()
    def restoreIpAddresses(self, s: str) -> List[str]:
        def rec(idx, reqSize, parts):
            if (idx == len(s) and reqSize == 0 and len(parts) == 4):
                self.Ans.append(parts)
                return
            if (idx == len(s) or reqSize == 0):
                return
            if len(parts) > 4 or idx >= len(s):
                return
            rec(idx+1, reqSize-1, parts + [ s[idx:idx+1] ])
            if s[idx] != "0":
                rec(idx+2, reqSize-2, parts + [s [idx:idx+2] ])
            if s[idx:idx+3] < "256" and s[idx] != "0":
                rec(idx+3, reqSize-3, parts + [s [idx:idx+3] ])
        rec(0, len(s), [])
        ans = []
        for item in self.Ans:
            ans.append(".".join(item))
        return ans