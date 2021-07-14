/*
1927. Sum Game

Alice and Bob take turns playing a game, with Alice starting first.

You are given a string num of even length consisting of digits and '?' characters. On each turn, a player will do the following if there is still at least one '?' in num:

Choose an index i where num[i] == '?'.
Replace num[i] with any digit between '0' and '9'.
The game ends when there are no more '?' characters in num.

For Bob to win, the sum of the digits in the first half of num must be equal to the sum of the digits in the second half. For Alice to win, the sums must not be equal.

For example, if the game ended with num = "243801", then Bob wins because 2+4+3 = 8+0+1. If the game ended with num = "243803", then Alice wins because 2+4+3 != 8+0+3.
Assuming Alice and Bob play optimally, return true if Alice will win and false if Bob will win.



Example 1:

Input: num = "5023"
Output: false
Explanation: There are no moves to be made.
The sum of the first half is equal to the sum of the second half: 5 + 0 = 2 + 3.
Example 2:

Input: num = "25??"
Output: true
Explanation: Alice can replace one of the '?'s with '9' and it will be impossible for Bob to make the sums equal.
Example 3:

Input: num = "?3295???"
Output: false
Explanation: It can be proven that Bob will always win. One possible outcome is:
- Alice replaces the first '?' with '9'. num = "93295???".
- Bob replaces one of the '?' in the right half with '9'. num = "932959??".
- Alice replaces one of the '?' in the right half with '2'. num = "9329592?".
- Bob replaces the last '?' in the right half with '7'. num = "93295927".
Bob wins because 9 + 3 + 2 + 9 = 5 + 9 + 2 + 7.


Constraints:

2 <= num.length <= 105
num.length is even.
num consists of only digits and '?'.
*/

func strToNum(num string) int {
	ans := 0
	for _, ch := range num {
		if ch == '?' {
			continue
		}
		parsed, _ := strconv.Atoi(string(ch))
		ans += parsed
	}
	return ans
}

func sumGame(num string) bool {
	mid := len(num) / 2
	lnumQ := strings.Count(num[:mid], "?")
	rnumQ := strings.Count(num[mid:], "?")
	firstHalf := strToNum(num[:mid])
	secondHalf := strToNum(num[mid:])

	diffQ := lnumQ - rnumQ
	// If left and right have equal number of Q, They will cancel each other out
	if diffQ == 0 {
		if firstHalf == secondHalf {
			return false
		}
		return true
	}

	// Just handle the more Q on left side.
	if diffQ > 0 {
		if diffQ == 1 {
			return true
		}

		// Alice plays to spoil
		diffQ++
		if firstHalf+(9*int(diffQ/2)) != secondHalf {
			return true
		}

		// Bob plays to win
		diffQ--
		if firstHalf+(9*int(diffQ/2)) != secondHalf {
			return true
		}
		return false
	}

	// Just handle the more Q on left side.
	if diffQ < 0 {
		diffQ := rnumQ - lnumQ
		if diffQ == 1 {
			return true
		}

		// Alice plays to spoil
		diffQ++
		if secondHalf+(9*int(diffQ/2)) != firstHalf {
			return true
		}

		// Bob plays to win
		diffQ--
		if secondHalf+9*int(diffQ/2) != firstHalf {
			return true
		}
		return false
	}

	return false
}

