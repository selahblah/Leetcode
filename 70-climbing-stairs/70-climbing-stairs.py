class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n<=2: 
            return n
        
        dp = [0]*(n)
        dp[0] = 1
        dp[1] = 2
        for i in range(2,n):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n-1]
        
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