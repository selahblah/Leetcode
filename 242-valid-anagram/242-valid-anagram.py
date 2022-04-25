class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        ls = list(s)
        ts = list(t)
        index = 0
        
        for i in range(len(ls)):
            if ls[i] in ts:
                ts.remove(ls[i])
            else:
                break
            index += 1
                
        if index == len(t) == len(s):
            return True
        else:
            return False
            