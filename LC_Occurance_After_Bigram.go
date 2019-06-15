"""
1078. Occurrences After Bigram

Given words first and second, consider occurrences in some text of the form "first second third", where second comes immediately after first, and third comes immediately after second.

For each such occurrence, add "third" to the answer, and return the answer.

 

Example 1:

Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
Output: ["girl","student"]
Example 2:

Input: text = "we will we will rock you", first = "we", second = "will"
Output: ["we","rock"]
 

Note:

1 <= text.length <= 1000
text consists of space separated words, where each word consists of lowercase English letters.
1 <= first.length, second.length <= 10
first and second consist of lowercase English letters.
"""

func findOcurrences(text string, first string, second string) []string {
    Ans := make([]string,0)
    hash := make(map[string] bool)
    sliceText := strings.Split(text, " ")
    for _, item := range sliceText {
        if (hash[first] && hash[second]) {
            Ans = append(Ans, item)
            hash[first] = false
            hash[second] = false
        }
        
        if (item == first){
            hash[first] = true
            hash[second] = false
        } else if (item == second && hash[first] == true) {
            hash[second] = true
        } else {
            hash[first] = false
            hash[second] = false
        }
    }
    return Ans
}