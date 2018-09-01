"""
867. 4 Keys Keyboard
Imagine you have a special keyboard with the following keys:

Key 1: (A): Print one 'A' on screen.

Key 2: (Ctrl-A): Select the whole screen.

Key 3: (Ctrl-C): Copy selection to buffer.

Key 4: (Ctrl-V): Print buffer on screen appending it after what has already been printed.

Now, you can only press the keyboard for N times (with the above four keys), find out the maximum numbers of 'A' you can print on screen.

Example
Given N = 3, return 3.

Explanation:
We can at most get 3 A's on screen by pressing following key sequence:
A, A, A
Given N = 7, return 9.

Explanation:
We can at most get 9 A's on screen by pressing following key sequence:
A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V
Notice
1 <= N <= 50
Answers will be in the range of 32-bit signed integer.

6
"""

class Solution:
    """
    @param N: an integer
    @return: return an integer


    When N is less than 7, N is the answer
    pasteA select copy paste
    the best way invlves.. selecting a big chunck.. copying and pasting it multiple times.
    for check for N-3 to 1... and find the max length possible.
    1 2 3 4 5 6 7.
    lets assume we are at 7... It will take 3 tries to select copy and paste so consider N-3 element to 1.
    in our case... 4 is the N-3 rd element.
    When you are copying at 4... select step will select [1 2 3 4]..
    copy will copy the same.. and paste will paste it.

    N - bp + 1 (for the selected element ) -2 (for the select and copy stage)
    N-bp+1-2
    N-bp-1 is the multiplicant

    for this, we will have to consider
    """
    def maxA    (self, N):
        # write your code here
        dp = [0 for i in range(N+1)]
        for i in range(1,7):
            dp[i] = i
        for i in range(7,N+1):
            dp[i] = i
            for bp in range(N-3,0,-1):
                dp[i] = max(dp[i], dp[bp]*(i-bp-1))
        return dp[N]
