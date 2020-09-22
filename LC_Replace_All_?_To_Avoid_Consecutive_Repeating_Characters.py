"""

1576. Replace All ?'s to Avoid Consecutive Repeating Characters

Given a string s containing only lower case English letters and the '?' character, convert all the '?' characters into lower case letters such that the final string does not contain any consecutive repeating characters. You cannot modify the non '?' characters.

It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.

Return the final string after all the conversions (possibly zero) have been made. If there is more than one solution, return any of them. It can be shown that an answer is always possible with the given constraints.

 

Example 1:

Input: s = "?zs"
Output: "azs"
Explanation: There are 25 solutions for this problem. From "azs" to "yzs", all are valid. Only "z" is an invalid modification as the string will consist of consecutive repeating characters in "zzs".
Example 2:

Input: s = "ubv?w"
Output: "ubvaw"
Explanation: There are 24 solutions for this problem. Only "v" and "w" are invalid modifications as the strings will consist of consecutive repeating characters in "ubvvw" and "ubvww".
Example 3:

Input: s = "j?qg??b"
Output: "jaqgacb"
Example 4:

Input: s = "??yw?ipkj?"
Output: "acywaipkja"
 

Constraints:

1 <= s.length <= 100

s contains only lower case English letters and '?'.

"""

class Solution(object):
    def modifyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        def generate(num, start, end):
            for i in range(ord('a'), ord('z')+1):
                if (str(chr(i)) != start and str(chr(i)) != end):
                    if (num == 1):
                        return chr(i), True
                    subStr, retVal = generate(num-1, chr(i), end)
                    if (retVal == True):
                        return chr(i) + subStr , True
            return "" ,False
        count = 0
        before, after = "", ""
        Ans = ""
        for ch in s:
            if (ch != "?"):
                if (count > 0):
                    after = ch
                    gen, _ = generate(count, before, after)
                    Ans += before + gen 
                    after = ""
                    before = ""
                    count = 0
                if (before != ""):
                    Ans += before
                before = ch
            elif (ch == "?"):
                count += 1
        if (before != ""):
            Ans += before
        if (count > 0):
            gen,_ = generate(count, before, "")
            Ans += gen
        
        return Ans
                
        
                    