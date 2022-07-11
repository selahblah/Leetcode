class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1: return True
        l,r = 0, num
        while l<=r:
            m = l+(r-l)//2
            if m**2 == num: return True
            elif m**2 < num: l = m+1
            else: r = m-1
        return False