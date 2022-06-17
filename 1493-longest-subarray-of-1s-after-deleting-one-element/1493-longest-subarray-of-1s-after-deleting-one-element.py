class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 0
        if 0 not in nums: return len(nums)-1
        while j <len(nums) and nums[j] == 0: nums = nums[1:]
        
        res = past_one = i = zero = 0
        while i < len(nums):
            one = zero = 0
            while i < len(nums) and nums[i] == 1: 
                one += 1
                i += 1
            while i < len(nums) and nums[i] == 0: 
                zero += 1
                i += 1
            res = max(res, past_one + one)
            if zero > 1: past_one = 0
            else: past_one = one
        
        return res
                
            