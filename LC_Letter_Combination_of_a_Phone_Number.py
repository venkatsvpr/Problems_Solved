# Solution to Letter Combination of Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        Ans =[]
        char_list = [["a","b","c"],["d","e","f"],["g","h","i"],["j","k","l"],["m","n","o"],["p","q","r","s"],["t","u","v"],["w","x","y","z"]]

        def Combination (S = '',index = 0):
            if index == len(digits):
                Ans.append(S)
                return
            
            list1 = char_list[int(digits[index])-2]
            for elem in list1:
                Combination (S+elem, index+1)
        
        if (digits != ""):
            Combination();

        return Ans
