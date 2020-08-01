`
1422. Maximum Score After Splitting a String

Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

 

Example 1:

Input: s = "011101"
Output: 5 
Explanation: 
All possible ways of splitting s into two non-empty substrings are:
left = "0" and right = "11101", score = 1 + 4 = 5 
left = "01" and right = "1101", score = 1 + 3 = 4 
left = "011" and right = "101", score = 1 + 2 = 3 
left = "0111" and right = "01", score = 1 + 1 = 2 
left = "01110" and right = "1", score = 2 + 1 = 3
Example 2:

Input: s = "00111"
Output: 5
Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5
Example 3:

Input: s = "1111"
Output: 3
 

Constraints:

2 <= s.length <= 500
The string s consists of characters '0' and '1' only.

`
func maxScore(s string) int {
    leftToRight := []int{}
    rightToLeft := []int{}
    zeroCount := 0
    for _, ch := range s {
        if (ch == '0'){
            zeroCount++
        }
        leftToRight = append(leftToRight, zeroCount)
    }
    
    oneCount := 0
    revStr := Reverse(s)
    for _,ch := range revStr {
        if (ch == '1'){
            oneCount++
        }
        rightToLeft = append(rightToLeft, oneCount)
    }

    i := 0
    j := len(rightToLeft) - 1
    for i < j {
        rightToLeft[i], rightToLeft[j] = rightToLeft[j], rightToLeft[i]
        i++
        j--
    }
    
    maxVal := 0
    for i := 0; i < len(leftToRight)-1 ; i++ {
        if (leftToRight[i]+rightToLeft[i+1] > maxVal) {
            maxVal = leftToRight[i]+rightToLeft[i+1]
        }
    }
    
    return maxVal
}

func Reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}