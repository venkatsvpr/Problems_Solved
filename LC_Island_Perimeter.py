# https://leetcode.com/problems/island-perimeter/description/
# Island Perimeter 
class Solution(object):
    def islandPerimeter(self, grid):
        count = 0;
        prev = -10;
        for lt in grid:
            prev = -1
            for item in lt:
                if (prev == -1):
                    if (item == 1):
                        count += 1
                    prev = item
                    continue;
                
                if (prev != item):
                    count += 1
                    prev = item
            if (prev == 1):
                count+=1
                
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        prev = -1
        grid2 = map(list, zip(*grid))

        for lt in grid2:
            prev = -1
            for item in lt:
                if (prev == -1):
                    if (item == 1):
                        count += 1
                    prev = item
                    continue;
                
                if (prev != item):
                    count += 1
                    prev = item
            if (prev == 1):
                count+=1
        return count
