class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3: return 0
        res, i = 0, 0
        
        while i < len(nums)-1:
            diff = nums[i+1] - nums[i]
            tem1, tem2 = 0, 0
            i += 1
            while i < len(nums)-1 and nums[i+1] - nums[i] == diff:
                tem1 += 1
                tem2 += tem1
                i += 1
            res += tem2
        
        return res
            
        
            