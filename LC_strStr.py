class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n_index = 0
        if (0 == len(needle)):
            return -1
        for index,char in enumerate(haystack):
            if (n_index == len(needle)):
                return index-n_index
            if (char == needle[n_index]):
                n_index += 1
            else:
                n_index = 0
        return -1
