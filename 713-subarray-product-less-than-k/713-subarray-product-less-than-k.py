class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left, res, sub, pro = 0, 0, 0, 1
        
        for i in range(len(nums)):
            pro *= nums[i]
            sub += 1
            
            while pro >= k and left < i:
                pro /= nums[left]
                left += 1
                sub -= 1
            
            if pro < k:
                res += sub
                
        return res
            
        
            
            