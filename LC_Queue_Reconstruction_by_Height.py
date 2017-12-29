# Queue Reconstruction by height
# https://leetcode.com/problems/queue-reconstruction-by-height/submissions/1
class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        answer = []    
        if not people:
            return answer
        
        for p in sorted((-record[0], record[1]) for record in people):
            answer.insert(p[1], [-p[0], p[1]])
            
        return (answer)
            
