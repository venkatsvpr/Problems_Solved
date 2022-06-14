"""
539. Minimum Time Difference


Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
 

Example 1:

Input: timePoints = ["23:59","00:00"]
Output: 1
Example 2:

Input: timePoints = ["00:00","23:59","00:00"]
Output: 0
 

Constraints:

2 <= timePoints.length <= 2 * 104
timePoints[i] is in the format "HH:MM".

"""
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Create buckets, with one bucket per minute
        minutesInDay = [0] * (24 * 60)
        
        # Map the inputs to buckets.
        for timePoint in timePoints:
            spltTimePoint = timePoint.split(":")
            minute = int(spltTimePoint[0])*60 + int(spltTimePoint[1])
            minutesInDay[minute] += 1
            # If two starts time overlap then return 0 since we the min time difference will be zero
            if minutesInDay[minute] > 1:
                return 0
            
        
        minTimeDiff = float('inf')
        pastTime = 0
        
        # Run over minutes to account for time rollover. 
        for idx,time in enumerate(minutesInDay+minutesInDay):
            # We are interested in points which have a non zero value
            if time <= 0:
                continue
            if pastTime >0 and idx-pastTime < minTimeDiff:
                minTimeDiff = idx-pastTime
            pastTime = idx
        return minTimeDiff
            
            
            
        
        
            
            
            
        
        