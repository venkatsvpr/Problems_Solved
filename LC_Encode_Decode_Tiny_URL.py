"""
Encode Decode Tiny URL
https://leetcode.com/problems/encode-and-decode-tinyurl/description/
"""

from random import choice


class Codec:
    sMatch ="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self):
        self.Master_dict = {}
        
    def encode(self, longUrl):
        if not longUrl:
            return
        """Encodes a URL to a shortened URL. 
    
        :type longUrl: str
        :rtype: str
        """
        hash_value = hash(longUrl)
        sURL = ""
        
        """
        Randomly generate it for 6 digits
        """
        digit = 6
        while(digit):
            sURL += random.choice(self.sMatch)
            digit = digit -1
        
        self.Master_dict[sURL] = longUrl;
        return "http://tinyurl.com/"+sURL

    def decode(self, shortUrl):
        if not shortUrl:
            return
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        new_str = shortUrl.replace("http://tinyurl.com/","")
        return self.Master_dict[new_str]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
