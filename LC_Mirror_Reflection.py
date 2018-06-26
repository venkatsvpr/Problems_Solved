"""
858. Mirror Reflection
There is a special square room with mirrors on each of the four walls.  Except for the southwest corner, there are receptors on each of the remaining corners, numbered 0, 1, and 2.

The square room has walls of length p, and a laser ray from the southwest corner first meets the east wall at a distance q from the 0th receptor.

Return the number of the receptor that the ray meets first.  (It is guaranteed that the ray will meet a receptor eventually.)



Example 1:

Input: p = 2, q = 1
Output: 2
Explanation: The ray meets receptor 2 the first time it gets reflected back to the left wall.



Note:

1 <= p <= 1000
0 <= q <= p
Approach:
=========
1) Continuosly divide p,q by 2 till one of p,q is odd.
2) If p and q are odd.  return 1
3) If p is odd.. and q is even  return 0
4) If p is even and q is odd return 2
"""
class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        def is_odd (n):
            if (n%2 == 0):
                return False
            return True

        def is_even (n):
            if (is_odd(n)):
                return False
            return True


        # Divide by 2 till either of it cannot be divided
        while ((p%2 == 0) and (q%2 == 0)):
            p = p/2
            q = q/2

        if (is_odd(p) and is_odd(q)):
            return 1
        if (is_odd(p) and is_even(q)):
            return 0
        if (is_even(p) and is_odd(q)):
            return 2
