class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        n = len(arr)
        dp = {}
        res = 0
        
        for num in arr:
            target = num-difference
            
            if target not in dp:
                dp[num] = 1
            else:
                dp[num] = 1 + dp[target]
            
            res = max(res,dp[num])
        return res