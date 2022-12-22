class Solution(object):
    def containsNearbyDuplicate(self, nums, key):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hash={}
        for i , v in enumerate(nums):
            if (v in hash and i-hash[v]<=key):
                return True
            hash[v]=i
        return False