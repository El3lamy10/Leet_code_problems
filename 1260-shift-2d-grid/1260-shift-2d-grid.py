class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        row=len(grid) #num of rows
        col=len(grid[0]) #num of colms
        #covert 2-D to vector
        def matToVec(r,c):
            return r*col+c
        #convert vector to 2-D
        def vecToMat(v):
            return [v//col,v%col]
        res=[[0] *col for i in range(row)]
        for i in range(row):
            for j in range(col):
                newpos=(matToVec(i,j)+k)%(row*col)
                newRow,newCol=vecToMat(newpos)
                res[newRow][newCol]=grid[i][j]
        return res