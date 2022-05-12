# https://leetcode.com/problems/trapping-rain-water/description/
# Trapping Rain Water
class Solution(object):
    def trap(self, height):
        start_elem = 0;
        lt =[]
        total_trap = 0;
        for element in height:
            if (start_elem == 0):
                start_elem = element
            elif (element >= start_elem):
                lt[:] = [abs(x-start_elem) for x in lt]
                total_trap += sum(lt);
                lt=[]
                start_elem = element
            elif (element < start_elem):
                lt.append(element)   
        lt=[]
        start_elem = 0;
        for element in reversed(height):
            if (start_elem == 0):
                start_elem = element
            elif (element > start_elem):
                lt[:] = [abs(x-start_elem) for x in lt]
                total_trap += sum(lt);
                lt=[]
                start_elem =element
            elif (element < start_elem):
                lt.append(element)   
     
        return total_trap


class Solution(object):
    def trap(self, height):
        # consider the equal case only in one direction to avoid double counting
        def calculate(ht, considerEqual):
            start_elem = 0;
            lt =[]
            total_trap = 0;
            for element in ht:
                if (start_elem == 0):
                    start_elem = element
                elif (element > start_elem) or (considerEqual and element == start_elem):
                    lt[:] = [abs(x-start_elem) for x in lt]
                    total_trap += sum(lt);
                    lt=[]
                    start_elem = element
                elif (element < start_elem):
                    lt.append(element)   
            return total_trap
        ans = 0
        # start from start and go to end calculate increase
        ans += calculate(height, True)
        # reverse the heights and do the same
        ans += calculate(reversed(height), False)
        return ans