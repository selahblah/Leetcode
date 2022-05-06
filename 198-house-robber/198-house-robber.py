class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums)==0: return 0
        
        dp = [0]*(len(nums)+1)
        
        dp[0] = 0
        dp[1] = nums[0]
        
        i=1
        while i < len(nums): 
            dp[i+1] = max(dp[i],dp[i-1]+nums[i])
            i += 1
            
        return dp[len(nums)]