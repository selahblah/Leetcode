class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        """
        for x in s:
            if not x in t: return False
            else: 
                ind = t.index(x)
                t = t[ind+1:]
        return True
        """
        stack = list(s)
        for char in t:
            if stack and stack[0] == char:
                stack.pop(0)
        return stack == []
        
            