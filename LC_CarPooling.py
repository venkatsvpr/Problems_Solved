"""
1094. Car Pooling
There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

 

Example 1:

Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
Example 2:

Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true
 

Constraints:

1 <= trips.length <= 1000
trips[i].length == 3
1 <= numPassengersi <= 100
0 <= fromi < toi <= 1000
1 <= capacity <= 105

"""
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        def mediumSolve(trips, maxCapacity):
            # doing the same as best.. but we use O(NlogN)
            timeSeries = []
            for [cap, start, end] in trips:
                timeSeries.append([start,cap])
                timeSeries.append([end, -cap])
            timeSeries.sort()
            
            usedCap = 0
            for [t, cap] in timeSeries:
                usedCap += cap
                if usedCap > capacity:
                    return False
            return True
        
        def bestSolve(trips, maxCapacity):
            # Move the points to timeSeries (discrete time series events)
            timeSeries = [0] * 1001
            for [cap, start, end] in trips:
                timeSeries[start] += cap
                timeSeries[end] -= cap
            
            # Keep track of the used capacity
            usedCap = 0
            for cap in timeSeries:
                usedCap += cap
                # Anytime we want more than the max capacity bail out
                if usedCap > maxCapacity:
                    return False
            return True
        return mediumSolve(trips, capacity)
            
        