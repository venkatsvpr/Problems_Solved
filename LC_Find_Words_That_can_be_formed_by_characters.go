```
1160. Find Words That Can Be Formed by Characters

You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

 

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: 
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: 
The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
 

Note:

1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
All strings contain lowercase English letters only.
```
func countCharacters(words []string, chars string) int {
    mapOfChars := make(map[string]int)
    for _,item := range(chars) {
        mapOfChars[string(item)]++
    }
    Ans := int(0)
    for _,word := range(words) {
        wordMap := make(map[string]int)
        for _,item := range(word) {
            wordMap[string(item)]++
        }
        success := true
        for key,_ := range(wordMap) {
            if (wordMap[string(key)] > mapOfChars[string(key)]) || (mapOfChars[string(key)] == 0) {
                success = false
                break
            }
        }
        if (success) {
            Ans += len(word)
        }
    }
    return Ans
}