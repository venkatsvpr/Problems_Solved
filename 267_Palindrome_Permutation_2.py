class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        count = collections.Counter(s)
        oddCount = 0
        for c in range(ord('a'), ord('z')+1):
            ch = chr(c)
            if count[ch]  % 2 != 0:
                oddCount += 1
        
        # If we have more than one odd point, we cannot make a palindrome
        if oddCount > 1:
            return []
        
        # If there is unit size string, return 1
        if len(s) == 1:
            return [s]
        oddChr = ""
        
        # We just need one half, restis going to be mirror
        for c in range(ord('a'), ord('z')+1):
            ch  = chr(c)
            if count[ch] %2 != 0:
                oddChr = ch
                count[ch] -= 1
                break

        input1 = ""
        for c in range(ord('a'), ord('z')+1):
            ch = chr(c)
            if count[ch] > 0:
                count[ch] = count[ch]//2
                input1 += ch * count[ch]
        
        res  = set()
        # Construct one half
        def backtrack(st, cin):
            if cin == "":
                res.add(st + oddChr + st[::-1])
                return
            
            for i,ch in enumerate(cin):
                backtrack(st+ch, cin[:i]+cin[i+1:])
            return
        backtrack("", input1)
        return list(res)      
                
            
