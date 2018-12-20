"""
Have a cell array.. and perform transtions.
keep a copy of the cell transformation
whenver we see a cell that is already seen... keep track of the difference and perform only the offset lookup

"""
class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        # Perform transition
        def transform (cell):
            NewCell = [0 for i in range(len(cell))]
            for i in range(1,len(cell)-1):
                if (cell[i-1] == cell[i+1]):
                    NewCell[i] = 1
            NewCell[0] = 0
            NewCell[len(cell)-1] = 0
            return NewCell
        # Keep a cache to store the history of transnformation
        cache = dict()
        cache[tuple(cells)] = 0
        i = 1
        # Keep doing it
        while (i <= N):
            cells = transform(cells)
            if (tuple(cells) in cache):
                pastIdx = cache[tuple(cells)]
                offset = i - pastIdx
                if (offset == 1):
                    return cells
                newIndex = N%offset
                if (newIndex == 0):
                    newIndex = i-pastIdx
                for key in cache:
                    if (cache[key] == newIndex):
                        return list(key)
            else:
                cache[tuple(cells)] = i
            i += 1
        return cells