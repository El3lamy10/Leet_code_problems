import re
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res=[]*len(words)
        for word in words:
            if re.match("^[qwertyuiop]+$", word.lower()) or re.match("[asdfghjkl]+$", word.lower()) or re.match("[zxcvbnm]+$", word.lower()):
                    
                    res.append(word)
        return res
