class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        lst = []
        minm = max(arr)
        for i in range(1,len(arr)):
            prev=arr[i-1]
            cur=abs(prev-arr[i])
            if cur<minm:
                lst=[[prev,arr[i]]]
                minm=cur
            elif cur==minm:
                lst.append([prev,arr[i]])

        return lst
