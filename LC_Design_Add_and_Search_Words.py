"""
211. Design Add and Search Words Data Structure


Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
 

Constraints:

1 <= word.length <= 25
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 3 dots in word for search queries.
At most 104 calls will be made to addWord and search.
"""

class Node:
    def __init__(self):
        self.next = collections.defaultdict(dict)
        self.isWord = False
class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.next:
                node.next[ch] = Node()
                node = node.next[ch]
            else:
                node = node.next[ch]
        node.isWord = True
    def search(self, word: str) -> bool:
        def rec(word, node):
            if len(word) == 0:
                return node.isWord
            ch = word[0]
            if ch == ".":
                for k in node.next:
                    if rec(word[1:], node.next[k]) == True:
                        return True
            else:
                if ch not in node.next:
                    return False
                if True == rec(word[1:],node.next[ch]):
                    return True
            return False
        node = self.root
        return rec(word, node)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)