# Reverse Vowels in a String
# https://leetcode.com/problems/reverse-vowels-of-a-string/description/
class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels ="aeiouAEIOU"
        str = list(s)
        index1 = index2 = 0;
        i = 0;
        index2 = len(str)-1;
        j = index2;
        k=0;
        char = char2 = ''
        
        while (1):
            #print (str);
            #print ("index1",index1,"index2",index2)
            if (index1 >= index2):
                break;
            
            for i in range(index1, j+1):
               # print ("looping i",i,"index1",index1,"i",i,"j",j)
                char = str[i]
                if char in vowels:
                  #  print ("in vowel ->",char)
                    index1 = i+1
                    break;
            
            if (i >= index2):
                break;
                    
            for j in range(index2, i-1, -1):
               # print ("looping j",j,"index2",index2,"i",i,"j",j)
                char2 = str[j]
                if char2 in vowels:
                  #  print ("in vowel --->",char2)
                    index2 = j-1
                    break;
            
            
            #print ("chars ",char,char2)
            if (char in vowels and char2 in vowels):
               # print (char,char2,"---swap",index1,index2)
                str[index2+1] = char
                str[index1-1] = char2
                continue;
        
        return ''.join(str)
        
