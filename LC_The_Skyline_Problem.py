"""
218. The Skyline Problem
==========================
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), write a program to output the skyline formed by these buildings collectively (Figure B).

Buildings  Skyline Contour
The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left and right edge of the ith building, respectively, and Hi is its height. It is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height. Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:

The number of buildings in any input list is guaranteed to be in the range [0, 10000].
The input list is already sorted in ascending order by the left x position Li.
The output list must be sorted by the x position.
There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]

Approach:
========
1) write a sort function to sort it.. star_i < start_j ....
If both starts are same..
if (height_i < height_j) if i is end and j is start .. consider j before i
                         if i is start and j is start.. consider j before i
                         if i is start and j is end  consider i before j
                         if i is end and j is end .. consider i  before j

At starts the heights to  priority queue.. if the max changes add it Answer
at ends remove the height from the priority queue.. if the max changes..
add it answer.. with the then max.

"""
import functools
import queue as Q
class Solution:
    max_elem = float('-inf')
    todelete = dict()
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        def cmp(a,b):
            if (a[0] != b[0]):
                return a[0]-b[0]
            else:
                if (a[1] == b[1]):
                    if (a[2] == "s"):
                        if (b[2] == "s"):
                            return 1;
                        else:
                            return -1
                    else:
                        if (b[2] == "s"):
                            return 1
                        else:
                            return -1
                elif (a[1] > b[1]):
                    if (a[2] == "s"):
                        if (b[2] == "s"):
                            return -1
                        else:
                            return -1
                    else:
                        if (b[2] == "s"):
                            return 1
                        else:
                            return 1
                elif (a[1] < b[1]):
                    if (b[2] == "s"):
                        if (a[2] == "s"):
                            return 1
                        else:
                            return 1
                    else:
                        if (a[2]== "s"):
                            return -1
                        else:
                            return -1

        # add to pq
        def add_to_pq(pq,elem):
            if (elem > self.max_elem):
                self.max_elem = elem
                if (elem in self.todelete) and (self.todelete[elem] == True):
                    self.todelete[elem] = False
                else:
                    pq.put(-elem)
                return True
            else:
                if (elem in self.todelete) and (self.todelete[elem] == True):
                    self.todelete[elem] = False
                else:
                    pq.put(-elem)
                return False

        # clear values in the priority queue which are at the top of the priority queue
        # which are to be deleted
        def clear_old_values (pq):
            while (pq.qsize()):
                element =-1* pq.get()
                if (element not in self.todelete) or (self.todelete[element] == False):
                    pq.put(-element)
                    self.max_elem = element
                    return
                self.todelete[element] = False
            self.max_elem = float('-inf')
            return

        # api to delete pq
        def remove_from_pq(pq,elem):
            el1 = -1 * pq.get()
            if (el1 != elem):
                self.todelete[elem] = True
                pq.put(-el1)
                return False
            else:
                clear_old_values(pq)
                if (pq.qsize()):
                    el2 = -1 * pq.get()
                    if (el2 == elem):
                        pq.put(-el2)
                        return False
                    else:
                        pq.put(-el2)
                        return True
                else:
                    return True

        Input = []
        for item in buildings:
            Input.append([item[0],item[2],"s"])
            Input.append([item[1],item[2],"e"])

        NewInput = sorted(Input, key=functools.cmp_to_key(cmp))
        Ans = []
        pq = Q.PriorityQueue()

        for item in NewInput:
            if (item[2] == "s"):
                # If a start is seen add it to priority queue
                # if max value changes.. add it to Answer
                retval = add_to_pq(pq,item[1])
                if (retval == True):
                    Ans.append([item[0],item[1]])
            elif (item[2] == "e"):
                # If a end value is seen.. take it out of the priority queue
                # if max value changes.. add it to Answer
                retval = remove_from_pq(pq,item[1])
                if (retval == True):
                    if (self.max_elem == float("-inf")):
                        Ans.append([item[0],0])
                    else:
                        Ans.append([item[0],self.max_elem])
        return Ans
