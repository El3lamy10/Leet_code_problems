class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minmm=1
        currnt=0
        for i in nums:
            currnt+=i
            if currnt <0:
                minmm=max(minmm,-currnt+1)
        return minmm