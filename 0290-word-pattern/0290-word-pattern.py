class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s = pattern
        t = str.split()
        return map(s.find, s) == map(t.index, t)