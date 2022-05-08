class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0]*(len(nums)+1)
        dp[0] = 0
        dp[1] = nums[0]
        
        i = 1
        while i < len(nums):
            dp[i+1] = max(nums[i]+dp[i-1], dp[i])
            i += 1
        
        return dp[len(nums)]