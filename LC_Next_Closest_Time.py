"""
681. Next Closest Time
Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

Example 1:

Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.
Example 2:

Input: "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time is nex
"""


"""
Since the search space is limited.
we iterate over all the 4 digits..
- ignore all hours. which are greater than 24.. all minutes that are greater than 59
- calcualte the difference between the two values..if a differe is less than already minimum difference store tht.
- do modulo so as to round of for next day.. for exaample if given with 23:59. the next best time is 22:22 which can only
be found if we allow roundoff.. take modulo of 24*60
"""
class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        Input = list(time)
        Input = Input[:2] + Input[3:]
        # Calculate the current time
        mytime = (int(Input[0])*10 + int(Input[1])) * 60 + int(Input[2])*10 + int(Input[3])
        diff = 24 * 60
        Ans = []
        for a,b,c,d in itertools.product(Input, repeat = 4):
            hour =  10*int(a) + int(b)
            minute = 10*int(c) + int(d)
            if (hour > 24) or (minute >= 60):
                continue;
            # Calculate the next time
            nxttime = (hour * 60) + minute
            # find the difference
            newdiff = (nxttime - mytime) % (24 * 60)
            if (newdiff == 0):
                continue;
            if (newdiff < diff):
                diff = newdiff
                Ans = [a,b,c,d]
        # if we are not able to find the answer.. then the same number is repeated
        if (len(Ans) == 0):
            return time
        return "".join(Ans[:2])+":"+"".join(Ans[2:])
