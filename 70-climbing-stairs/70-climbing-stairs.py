class Solution:
    def climbStairs(self, n: int) -> int:
        """
        one, two = 1, 1
        
        while i <= n:
            tem = one
            one = one + two
            two = tem
            
        return one
        """
        
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]
        
        
        