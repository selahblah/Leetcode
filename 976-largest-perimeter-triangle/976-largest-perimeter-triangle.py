class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        for a,b,c in zip(nums[0:],nums[1:],nums[2:]):
            if a<b+c: return a+b+c
        
        return 0