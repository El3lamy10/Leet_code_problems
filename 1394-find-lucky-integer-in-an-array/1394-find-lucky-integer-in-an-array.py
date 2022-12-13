class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        hash={}
        res=-1
        for i in arr:
            if i in hash:
                hash[i]+=1
            else:
                hash[i]=1
        for i in hash:
            if i==hash[i]:
                
                res=max(res,i)
        return res
            