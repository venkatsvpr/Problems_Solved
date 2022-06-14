"""
1166. Design File System

You are asked to design a file system that allows you to create new paths and associate them with different values.

The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters. For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string "" and "/" are not.

Implement the FileSystem class:

bool createPath(string path, int value) Creates a new path and associates a value to it if possible and returns true. Returns false if the path already exists or its parent path doesn't exist.
int get(string path) Returns the value associated with path or returns -1 if the path doesn't exist.
 

Example 1:

Input: 
["FileSystem","createPath","get"]
[[],["/a",1],["/a"]]
Output: 
[null,true,1]
Explanation: 
FileSystem fileSystem = new FileSystem();

fileSystem.createPath("/a", 1); // return true
fileSystem.get("/a"); // return 1
Example 2:

Input: 
["FileSystem","createPath","createPath","get","createPath","get"]
[[],["/leet",1],["/leet/code",2],["/leet/code"],["/c/d",1],["/c"]]
Output: 
[null,true,true,2,false,-1]
Explanation: 
FileSystem fileSystem = new FileSystem();

fileSystem.createPath("/leet", 1); // return true
fileSystem.createPath("/leet/code", 2); // return true
fileSystem.get("/leet/code"); // return 2
fileSystem.createPath("/c/d", 1); // return false because the parent path "/c" doesn't exist.
fileSystem.get("/c"); // return -1 because this path doesn't exist.
 

Constraints:

The number of calls to the two functions is less than or equal to 104 in total.
2 <= path.length <= 100
1 <= value <= 109

"""

# Create  trie and keep track of the path
# When spliting "/foo" there will be two items "" and "foo" - need to not worry about the first ""
class TrieNode:
    def __init__(self, name):
        self.value = -1
        self.children = defaultdict(TrieNode)
        self.name = name
        
class FileSystem:
    def __init__(self):
        self.root = TrieNode("")
    
    def createPath(self, path: str, value: int) -> bool:
        # Traverse the trie
        components = path.split("/")
        node = self.root
        for i in range(1,len(components)):
            name = components[i]
            if name not in node.children:
                # It is problem but for the last part of the path
                if i == len(components)-1:
                    node.children[name] = TrieNode(name)
                else:
                    return False
            node = node.children[name]

        ## Already something is prsent
        if node.value != -1:
            return False
        
        node.value = value
        return True
        

    def get(self, path: str) -> int:
        components = path.split("/")
        
        node = self.root
        # Traverse the Trie
        for i in range(1,len(components)):
            name = components[i]
            if name not in node.children:
                return -1
            node = node.children[components[i]]
        return node.value



# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)