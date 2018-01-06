"""
Queue Reconstruction by height
"""
class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        answer = []    
        if not people:
            return answer
        
        """  Sort the data by the decreasing height """
        lt = [[-item[0],item[1]] for item in people]     
        for p in sorted(lt):
            answer.insert(p[1], [-p[0], p[1]])
            """ Insert the data in the p[1] position """
        return (answer)
            
