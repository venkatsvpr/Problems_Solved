#solution to  https://www.hackerrank.com/contests/world-codesprint-12/challenges/red-knights-shortest-path/problem
# 7/11 cases pass.. other failing because the logic takes a different path
#!/bin/python

import sys

ans = []
count = 0


def is_same_type(i_start, i_end, j_start, j_end):
    if (i_end % 2 == 0):
        if (i_start % 2 != 0):
            return 0

    if (i_start % 2 == 0):
        if (i_end % 2 != 0):
            return 0

    return 1


def move_UL(i_start, j_start):
    global count
    ans.append("UL");
    count = count + 1
    return i_start - 2, j_start - 1


def move_UR(i_start, j_start):
    global count
    ans.append("UR");
    count = count + 1
    return i_start - 2, j_start + 1


def move_LL(i_start, j_start):
    global count
    ans.append("LL")
    count = count + 1
    return i_start + 2, j_start - 1


def move_LR(i_start, j_start):
    global count
    ans.append("LR")
    count = count + 1
    return i_start + 2, j_start + 1


def move_L(i_start, j_start):
    global count
    ans.append("L")
    count = count + 1
    return i_start, j_start - 2


def move_R(i_start, j_start):
    global count
    ans.append("R")
    count = count + 1
    return i_start, j_start + 2


def printShortestPath(n, i_start, j_start, i_end, j_end):
    if (i_start == i_end):
        if (j_start == j_end):
            return;

    if ((i_start < 0) or (j_start < 0)):
        return;

    i_max = 0;
    if (i_start > i_end):
        i_max = i_start
    else:
        i_max = i_end

    j_max = 0
    if (j_start > j_end):
        j_max = j_start
    else:
        j_max = j_end

    i_offset = abs(i_end - i_start);

    j_offset = abs(j_end - j_start);

    if (1):
        if (i_start == i_end):
            if (j_start < j_end):
                i_start, j_start = move_R(i_start, j_start)
            elif (j_start > j_end):
                i_start, j_start = move_L(i_start, j_start)
        elif (j_start == j_end):
            if (i_start > i_end):
                if (i_start < i_max):
                    i_start, j_start = move_UR(i_start, j_start)
                else:
                    i_start, j_start = move_UL(i_start, j_start)
            else:
                if (i_start < i_max):
                    i_start, j_start = move_LR(i_start, j_start)
                else:
                    i_start, j_start = move_LL(i_start, j_start)
        elif (i_start == i_max):
            if (j_start >= j_end):
                i_start, j_start = move_UL(i_start, j_start)
            elif (j_end > j_start):
                i_start, j_start = move_UR(i_start, j_start)
        elif (j_start == j_max):
            if (i_start >= i_end):
                i_start, j_start = move_UL(i_start, j_start)
            elif (i_start < i_end):
                i_start, j_start = move_LL(i_start, j_start)
        elif (i_start > i_end):
            if (j_start > j_end):
                i_start, j_start = move_UL(i_start, j_start)
            elif (j_start < j_end):
                i_start, j_start = move_UR(i_start, j_start)
        elif (i_start < i_end):
            if (j_start <= j_end):
                i_start, j_start = move_LR(i_start, j_start)
            elif (j_start > j_end):
                i_start, j_start = move_LL(i_start, j_start)
        else:
            return;
    printShortestPath(n, i_start, j_start, i_end, j_end)

    #  Print the distance along with the sequence of moves.


if __name__ == "__main__":
    n = int(raw_input().strip())
    i_start, j_start, i_end, j_end = raw_input().strip().split(' ')
    i_start, j_start, i_end, j_end = [int(i_start), int(j_start), int(i_end), int(j_end)]
    count = 0
    if (0 == is_same_type(i_start, i_end, j_start, j_end)):
        print
        "Impossible"
    else:
        printShortestPath(n, i_start, j_start, i_end, j_end)
        print
        count
        for string in ans:
            print(string),



