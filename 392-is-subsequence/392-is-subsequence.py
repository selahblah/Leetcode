class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        res = float("-inf")
        for x in s:
            if not x in t: return False
            else: 
                ind = t.index(x)
                t = t[ind+1:]
        return True
        
            