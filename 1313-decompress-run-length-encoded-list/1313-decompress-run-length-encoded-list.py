class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[]
        for i in range(1,len(nums),2):
            a+=[nums[i]]*nums[i-1]
        return(a)
    
#       ans = []
#         for i in range(0, len(nums), 2):
#             for j in range(nums[i]):
#                 ans.append(nums[i + 1])
#         return ans 