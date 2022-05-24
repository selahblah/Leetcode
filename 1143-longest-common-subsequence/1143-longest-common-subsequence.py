class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        n,m = len(text1), len(text2)
        dp = [[0]*(n+1) for i in range(m+1)]
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                if text1[i-1] == text2[j-1]:
                    dp[j][i] = dp[j-1][i-1]+1
                else: 
                    dp[j][i] = max(dp[j-1][i],dp[j][i-1])
                    
        return dp[-1][-1]