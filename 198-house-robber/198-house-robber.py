class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        tem1, tem2 = 0, 0
        for n in nums:
            res = max(tem1+n, tem2)
            tem1 = tem2
            tem2 = res
            
        return res