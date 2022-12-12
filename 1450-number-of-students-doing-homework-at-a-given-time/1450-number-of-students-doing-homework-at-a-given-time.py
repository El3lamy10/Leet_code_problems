class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        c=0
        for i in range(len(startTime)):          
            if startTime[i]<=queryTime<=endTime[i]:
                
                c+=1
        return c