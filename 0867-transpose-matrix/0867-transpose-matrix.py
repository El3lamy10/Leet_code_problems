import numpy as np
class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        arr1=np.array(matrix)
        arr2=arr1.transpose()
        return arr2