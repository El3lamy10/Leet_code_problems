class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        dif = (sum(A) - sum(B)) / 2
        A = set(A)
        for b in set(B):
            if dif + b in A:
                return [dif + b, b]