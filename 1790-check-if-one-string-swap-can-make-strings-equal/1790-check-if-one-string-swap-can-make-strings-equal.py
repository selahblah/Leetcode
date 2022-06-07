class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        has = []
        if s1 == s2: return True
        for i,j in enumerate(s1):
            if s2[i] == j: continue
            else:
                has.append([i,j])
                
        if len(has) != 2: return False
        else: 
            if s2[has[0][0]] == has[-1][-1] and s2[has[-1][0]] == has[0][-1]: return True
            else: return False
            