class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float("-inf")
        i = 0 
        while i < len(nums):
            tem = 0
            while i < len(nums) and tem >= 0:
                tem += nums[i]
                res = max(res, tem)
                i += 1
                
        return res