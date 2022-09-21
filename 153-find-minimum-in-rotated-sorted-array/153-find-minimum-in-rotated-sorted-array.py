class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,r = 0, len(nums)-1
        if nums[l] < nums[r]: return nums[l]
        elif len(nums)==1: return nums[0]
        
        while l <= r:
            m = l+(r-l)//2
            if nums[m-1] > nums[m]: return nums[m]
            elif nums[m] >= nums[l]: l += 1
            else: r -= 1
        return nums[l]