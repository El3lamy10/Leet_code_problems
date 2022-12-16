class Solution(object):
    def isToeplitzMatrix(self, m):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for i in range(1,len(m)):
            for j in range(1,len(m[0])):
                if m[i-1][j-1]!=m[i][j]:
                    return False
        return True