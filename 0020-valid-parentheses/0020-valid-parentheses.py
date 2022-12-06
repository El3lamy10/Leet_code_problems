class Solution:
    def isValid(self, s: str) -> bool:
        dct={')': '(', ']': '[', '}': '{'}
        stack=[]
        for char in s :
            if char not in dct:
                stack.append(char)
            elif not stack or dct[char]!=stack.pop():
                return False
        return not stack