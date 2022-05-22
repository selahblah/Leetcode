class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        N = len(s)
        dp = [False]*(N+1)
        dp[0] = True
        
        for start in range(len(s)):
            if not dp[start]: continue
            for end in range(start+1,len(dp)):
                if s[start:end] in wordDict: dp[end] = True
        
        return dp[-1]
        
        """
        sorted(wordDict,key=len)
        i = 0
        while i < len(wordDict):
            if wordDict[i] in s:
                s = s.replace(wordDict[i],"")
                print(s)
            else: return False
            i += 1
        
        return True
        """