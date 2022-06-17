class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        s_,p_ = list(s),list(part)
        i,len_ = 0, len(part)
        while i < len(s_)-len_+1:
            if s_[i:i+len_] == p_: 
                s_ = s_[:i]+s_[i+len_:]
                i -= len_
            else: i += 1
        return ''.join(s_)