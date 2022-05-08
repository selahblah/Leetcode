class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            tem = max(n+rob1, rob2)
            rob1 = rob2
            rob2 = tem
        return tem
        
        """
        dp = [0]*(len(nums)+1)
        dp[0] = 0
        dp[1] = nums[0]
        
        i = 1
        while i < len(nums):
            dp[i+1] = max(nums[i]+dp[i-1], dp[i])
            i += 1
        
        return dp[len(nums)]
        """