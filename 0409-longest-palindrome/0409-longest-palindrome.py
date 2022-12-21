class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash=set()
        for char in s:
            if char not in hash:
                hash.add(char)
            else:
                hash.remove(char)
        if len(hash)==0:
            return len(s)
        else: 
            return len(s)-len(hash)+1