"""
65. Valid Number


Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. However, here is a list of characters that can be in a valid decimal number:

Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."
Of course, the context of these characters also matters in the input.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button to reset your code definition.
"""

"""
Quite simple logic:
if we see a number we set numberseen and numberseenafter e as true
if we get a e. we check if have alreadyy ot e or if we have not got number.. in this case return false,
    set eseen as True and numseen after e as false
if we get . .. if we p or seen is seen return false..  set pseen
if +,-  it should be the first character or immediately after  e
if we get something else return false

"""
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        eSeen = False
        pSeen = False
        numSeen = False
        numESeen = False
        s = s.strip()
        for idx,ch in enumerate(s):
            if (ch >= "0" and ch <= "9"):
                numSeen = True
                numESeen = True
            elif (ch == "e"):
                if (eSeen == True) or (not numSeen):
                    return False
                eSeen  = True
                numESeen = False
            elif (ch == "."):
                if (pSeen or eSeen):
                    return False
                pSeen = True
            elif (ch == "+") or (ch == "-"):
                if not  ((idx == 0) or (s[idx-1] == "e")):
                    return False
            else:
                #print ("retu 29")
                return False
        return (numSeen and numESeen)
