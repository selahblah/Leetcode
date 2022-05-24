class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        N = len(s)
        dp = [False]*(N+1)
        dp[0] = True
        tem = ""
        
        for start in range(N):
            if dp[start] == False : continue
            else: 
                for end in range(start+1,N+1):
                    if s[start:end] in wordDict:
                        dp[end] = True
        print(dp)
                        
        return dp[-1]
                    