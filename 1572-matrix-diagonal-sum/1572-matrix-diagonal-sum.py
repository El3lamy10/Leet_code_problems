class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        ls=[]
        n=len(mat)
        for i in range(n):
            ls.append(mat[i][i])
            ls.append(mat[i][n - i - 1])
        if n%2==1:
            ls.remove(ls[len(ls)//2])
            return sum(ls[:])
        return sum(ls[:])