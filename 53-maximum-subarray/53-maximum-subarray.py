class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = tem = nums[0]
        i = 1
        while i < len(nums):
            while i < len(nums) and tem>=0:
                tem += nums[i]
                i += 1
                res = max(tem, res)
            tem = 0
        return res