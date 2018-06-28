"""
273. Integer to English Words
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"
Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
Approach
========
Things to keep in mind
1) 1 to 19 naming is differnt
2) other than that regular patters

"""


class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        def val (n):
            return ones[n]

        def value (n):
            if (n <20):
                return ones[n]
            divd  = 100
            ret = ""
            if (n/100 > 0):
                ret += val(n/100)+" Hundred"
                n = n%100
            if (n/10 >  1):
                if (len(ret) > 1):
                    ret += " "
                ret += twos[(n/10)-2]
                n = n%10
            if (n > 0):
                if (len(ret) > 2):
                    ret += " "
                ret += val(n)
            return ret

        ones = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen", "Sixteen","Seventeen","Eighteen","Nineteen"]
        twos = ["Twenty" ,"Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        big = ["Billion","Million","Thousand"]

        Ans = ""
        n = num

        if (n == 0):
            return "Zero"

        if (n/1000000000):
            Ans += value (n/1000000000)
            if (len(Ans) >0):
                Ans += " "
            Ans += "Billion"

        n = n%1000000000
        if (n/1000000):
            if (len(Ans) >0):
                Ans += " "
            Ans += value (n/1000000)
            Ans += " Million"

        n = n%1000000
        if (n/1000):
            if (len(Ans) >0):
                Ans += " "
            Ans += value (n/1000)
            Ans += " Thousand"

        n = n%1000
        if (n > 0):
            if (len(Ans)>0):
                Ans += " "
            Ans += value (n)
        if (Ans[0] == " "):
            return Ans[1:]
        return Ans
