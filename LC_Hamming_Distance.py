class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        """
        Do xor and check the number of bits
        """
        c = x ^ y
        count = 0
        while (c):
            count += 1
            c = c & (c-1)
        return (count)
