"""
739. Daily Temperatures


Given a list of daily temperatures, produce a list that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].


"""
"""
In the stack... always maintain desending order.

Create a stack and store the temperature and index.
1) if temp is greater than the top temperature on the stack
pop the top till temp is less than the top value in the stack.
for every item popped.. calculate the current_idx - popped_idx and store it n the answer
At the Ans [top_idx] = index - top_idx

2) else.. push the [temperature, index] into the stack

"""
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        Ans = [0] * len(temperatures)
        Stack = []
        for idx,temp in enumerate(temperatures):
            if (len(Stack) == 0):
                Stack.append([temp,idx])
                continue;
            while(len(Stack)):
                # If current temp is bigger than stack top keep popping the stack top operator
                # find best case answers and keep noting hte answer in the result.
                if (temp > Stack[-1][0]):
                    Ans[Stack[-1][1]] = idx-Stack[-1][1]
                    Stack.pop()
                else:
                    break;
            # While all the values  are popped out. Store the current temp and index into the Stack
            Stack.append([temp,idx])
        return Ans
                


class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        Ans = [0] * len(temperatures)
        Stack = []
        for idx,temp in enumerate(temperatures):
            while(len(Stack)):
                if (temp > Stack[-1][0]):
                    Ans[Stack[-1][1]] = idx-Stack[-1][1]
                    Stack.pop()
                else:
                    break;
            Stack.append([temp,idx])
        return Ans
                