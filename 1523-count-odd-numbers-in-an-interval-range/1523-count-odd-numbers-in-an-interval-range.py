class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """

        if high%2==0 and low%2==0: return (high-low)//2
        else: return (high-low)//2+1
        
        """
        for i in range(low,high+1):
            if i%2 == 1: res += 1
        return res
        """