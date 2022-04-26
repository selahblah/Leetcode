class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n<=2: 
            return n
        
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]
        
        """
        count = 0
        
        for x in range(n+1):
            for y in range(n//2+1):
                if x + 2*y == n:
                    count += 1
                elif x + 2*y < n:
                    pass
        return count
        """   