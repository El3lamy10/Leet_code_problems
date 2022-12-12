class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x=sorted(nums,reverse=True)
        return (x[0]-1)*(x[1]-1)