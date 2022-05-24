class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        n, m = len(word1), len(word2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(n+1):
            dp[0][i] = i
        for i in range(m+1):
            dp[i][0] = i
        
        for c in range(1,n+1):
            for r in range(1,m+1):
                if word1[c-1] == word2[r-1]:
                    dp[r][c] = dp[r-1][c-1]
                else: 
                    dp[r][c] = min(dp[r-1][c],dp[r][c-1])+1
        
        return dp[-1][-1]