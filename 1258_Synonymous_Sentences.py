"""
1258. Synonymous Sentences
Medium

289

124

Add to List

Share
You are given a list of equivalent string pairs synonyms where synonyms[i] = [si, ti] indicates that si and ti are equivalent strings. You are also given a sentence text.

Return all possible synonymous sentences sorted lexicographically.

 

Example 1:

Input: synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]], text = "I am happy today but was sad yesterday"
Output: ["I am cheerful today but was sad yesterday","I am cheerful today but was sorrow yesterday","I am happy today but was sad yesterday","I am happy today but was sorrow yesterday","I am joy today but was sad yesterday","I am joy today but was sorrow yesterday"]
Example 2:

Input: synonyms = [["happy","joy"],["cheerful","glad"]], text = "I am happy today but was sad yesterday"
Output: ["I am happy today but was sad yesterday","I am joy today but was sad yesterday"]
 

Constraints:

0 <= synonyms.length <= 10
synonyms[i].length == 2
1 <= si.length, ti.length <= 10
si != ti
text consists of at most 10 words.
All the pairs of synonyms are unique.
The words of text are separated by single spaces.

"""
class Solution:
    def __init__(self):
        self.rank = dict()
    
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        def find(word):
            if word not in self.rank:
                self.rank[word] = word
                return self.rank[word]
            if self.rank[word] == word:
                return word
            self.rank[word] = find(self.rank[word])
            return self.rank[word]
        
        def union(w1, w2):
            pw1 = find(w1)
            pw2 = find(w2)
            if pw1 == pw2:
                return
            self.rank[pw1] = pw2
            return
        
        def getWords(w1):
            w = []
            pw1 = find(w1)
            w.append(pw1)
            for word in self.rank:
                pw2 = find(word)
                if pw1 == pw2:
                    w.append(word)
            return list(set(w))
        
        for syn in synonyms:
            union(syn[0], syn[1])
        
        res = []
        words = text.split(" ")
        def rec(idx, history):
            if idx == len(words):
                cpy = history.copy()
                res.append(" ".join(cpy))
                return
            
            if words[idx] not in self.rank:
                return rec(idx+1, history + [words[idx]])
            
            for w2 in getWords(words[idx]):
                history.append(w2)
                rec(idx+1, history)
                history.pop()
            return
        rec(0, [])
        return sorted(res)
