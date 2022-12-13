# import numpy as np
class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        # arr1=np.array(matrix)
        # arr2=arr1.transpose()
        # return arr2
        
        
        r,c=len(matrix),len(matrix[0])
        trans=[[0 for i in range(r)]for j in range(c)]
        for i in range(r):
            for j in range(c):
                trans[j][i]=matrix[i][j]
        return trans