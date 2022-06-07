class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minus = 0
        for i in nums:
            if i == 0: return 0
            elif i < 0: minus += 1
                
        return -1 if minus%2 == 1 else 1