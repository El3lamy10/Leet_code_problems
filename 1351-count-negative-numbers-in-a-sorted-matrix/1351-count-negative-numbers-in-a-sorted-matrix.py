class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def binary(row):
            start=0
            end= len(row)
            while start<end:
                mid=start+ (end-start)//2
                if row[mid]<0:
                    end=mid
                else:
                    start=mid+1
            return len(row)-start
        cnt=0
        for row in grid:
            cnt+=binary(row)
        return cnt
    ##another sol O(n^2)
        # cnt=0
        # for i in range(len(grid)):
        #     for j in range(len(grid)):
        #         if grid[i][j]<0:
        #             cnt+=1
        # return cnt
