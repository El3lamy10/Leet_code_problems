class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n=len(arr)
        sum1 = 0
        for i in range(n):
            for j in range(i,n,2):
                sum1+=sum(arr[i:j+1])
        return sum1
                
