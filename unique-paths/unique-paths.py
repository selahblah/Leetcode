class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0 for col in range(n)] for row in range(m)]
        
        for row1 in range(n): dp[0][row1] = 1
        for col1 in range(m): dp[col1][0] = 1
        
        for col in range(1,n):
            for row in range(1,m):
                dp[row][col] = dp[row-1][col] + dp[row][col-1]
                
        return dp[m-1][n-1]
                
        """
        import math
        return int(math.comb(m+n-2,n-1))
    
        return int(math.factorial(m+n-2)/(math.factorial(m-1)*math.factorial(n-1)))
        """