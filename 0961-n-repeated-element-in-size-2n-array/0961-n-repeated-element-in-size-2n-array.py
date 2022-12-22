class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=[]
        for i in nums:
            if i in res:
                return i
            res.append(i)
        return res