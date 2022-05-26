class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        sqr = int(sqrt(c))
        s = set([a*a for a in range(sqr+1)])
        
        for a in s:
            b = c-a
            if b in s: return True
        return False
            
        
        """
        l,r = 0, int(c/2)+1
        while l <= r:
            sum2 = l**2 + r**2
            if sum2 == c: return True
            elif sum2 > c: r-=1
            else: l += 1
        
        return False
        """
            