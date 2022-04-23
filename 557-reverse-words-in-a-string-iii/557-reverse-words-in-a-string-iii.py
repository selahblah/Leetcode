class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        s_p = s.split()
        
        for i in range(len(s_p)):
             s_p[i] = s_p[i][::-1]
        return ' '.join(s_p)