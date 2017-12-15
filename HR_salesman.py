# https://www.hackerrank.com/contests/world-codesprint-12/challenges/the-salesman/problem
#!/bin/python

import sys

# Approach.- Sort the houses based on the distance. Sum of differences of
# Individual Houses distance difference.

def minimumTime(x):
    #  Return the minimum time needed to visit all the houses.
    prev = 0
    sum = 0

    for element in sorted(x):
        if (prev == 0):
            prev = element
            continue;
        sum = sum + abs(element - prev)
        prev = element
    return sum


if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in xrange(t):
        n = int(raw_input().strip())
        x = map(int, raw_input().strip().split(' '))
        result = minimumTime(x)
        print result

