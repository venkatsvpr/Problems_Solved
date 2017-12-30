# Letter Combination of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
# Iterative Solution
class Solution(object):
    def letterCombinations(self, digits):
        """
            :type digits: str
            :rtype: List[str]
            """
        Ans =[]
        char_list = [["a","b","c"],["d","e","f"],["g","h","i"],["j","k","l"],["m","n","o"],["p","q","r","s"],["t","u","v"],["w","x","y","z"]]
        for digit in digits:
            if (len(Ans) == 0):
                for item in char_list[int(digit)-2]:
                    Ans.append(item)
            else:
                NewAns=[]
                for element in Ans:
                    for item in char_list[int(digit)-2]:
                        NewAns.append(element+item)
                Ans = NewAns
        return Ans
