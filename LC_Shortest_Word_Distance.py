"""
Find the Shortest Word Distance.
Build a symbol table of position ofthe words in the word_list.

Then sort the positions of the two word seperately.
Run an algorithm where in we move the lowest of the two's index.
"""

class Solution:
    def shortestDistance(self, words, word1, word2):
        
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :type: int
        """
        def Find_Min_Difference (l1,l2,len1,len2):
            index1 = 0;
            index2 = 0;
            result = float('inf')
            while ((index1<len1) and (index2<len2)):
                if (abs(l1[index1]-l2[index2]) < result):
                    result = abs(l1[index1] - l2[index2])   
                
                if (l1[index1] < l2[index2]):
                    index1 += 1
                else:
                    index2 += 1
            return result  
        
        word1_loc = [i for i,x in enumerate(words) if x == word1]
        word2_loc = [i for i,x in enumerate(words) if x == word2]
        
        word1_loc = sorted(word1_loc)
        word2_loc = sorted(word2_loc)
        
        retval = Find_Min_Difference(word1_loc, word2_loc, len(word1_loc), len(word2_loc))
        
        return retval;
    
