class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        while s:
            while s and s[-1] != " ": 
                res += 1 
                s = s[:-1]
            if res!= 0: return res
            s = s[:-1]