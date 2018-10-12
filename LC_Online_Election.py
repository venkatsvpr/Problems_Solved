"""
911. Online Election


In an election, the i-th vote was cast for persons[i] at time times[i].

Now, we would like to implement the following query function: TopVotedCandidate.q(int t) will return the number of the person that was leading the election at time t.

Votes cast at time t will count towards our query.  In the case of a tie, the most recent vote (among tied candidates) wins.



Example 1:

Input: ["TopVotedCandidate","q","q","q","q","q","q"], [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
Output: [null,0,1,1,0,0,1]
Explanation:
At time 3, the votes are [0], and 0 is leading.
At time 12, the votes are [0,1,1], and 1 is leading.
At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the most recent vote.)
This continues for 3 more queries at time 15, 24, and 8.


Note:

1 <= persons.length = times.length <= 5000
0 <= persons[i] <= persons.length
times is a strictly increasing array with all elements in [0, 10^9].
TopVotedCandidate.q is called at most 10000 times per test case.
TopVotedCandidate.q(int t) is always called with t >= times[0].



Have an a list which contins... the winner of index i for the time at index i
Also store the player votes in a dictionary
do this.. and when we get a time... binary search and return the answer.
"""
class TopVotedCandidate(object):
    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.times = times
        self.winList = []
        self.playerCount = dict()
        self.winner = -1
        for p,t in zip(persons,times):
            if (self.winner == -1):
                self.winner = p
                self.playerCount[p] = self.playerCount.get(p,0)+1
                self.winList.append(self.winner)
                continue;
            self.playerCount[p] = self.playerCount.get(p,0)+1
            if (self.playerCount[p] >= self.playerCount[self.winner]):
                self.winner = p
            self.winList.append(self.winner)
        return
    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        def binarySearch (arr, search):
            low = 0
            high = len(arr)-1
            while (low <= high):
                #print (search,low,high,arr[low],arr[high])
                if (search < arr[low]):
                    return low-1
                if (search > arr[high]):
                    return high
                mid = (low+high)/2
                if (arr[mid] == search):
                    return mid
                if (arr[mid] > search):
                    high = mid-1
                if (arr[mid] < search):
                    low = mid+1
            return -1
        #print (self.winList)
        #print (self.times)
        item = binarySearch (self.times, t)
        #print (t,item)
        return self.winList[item]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
