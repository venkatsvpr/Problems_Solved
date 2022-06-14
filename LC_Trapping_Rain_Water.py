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


class Solution(object):
    def trap(self, height):
        # Find the max to the left
        max_left = [height[0]]
        for idx in range(1,len(height)):
            max_left.append(max(height[idx], max_left[-1]))
        
        # Find the max to the right
        max_right = [0 for i in range(len(height))]
        max_right[len(height)-1] = height[-1]
        for idx in range(len(height)-2,-1,-1):
            max_right[idx] = max(max_right[idx+1], height[idx])

        # Find the level, which would be min of the two maxes
        level = [min(max_left[idx], max_right[idx]) for idx in range(len(height))]
        
        # Find the water held, which would be level - height
        water = [level[idx] - height[idx] for idx in range(len(height))]
        return sum(water)
        
        
        