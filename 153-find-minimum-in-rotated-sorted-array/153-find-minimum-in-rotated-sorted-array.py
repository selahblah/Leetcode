class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,r = 0,len(nums)-1
        if nums[l] < nums[r]: return nums[l]
        while l<r:
            m = l+(r-l)//2
            if nums[m] > nums[m+1]: return nums[m+1]
            elif nums[m] > nums[l] and nums[m] > nums[r]: l = m+1
            elif nums[r] > nums[m]: r = m
        return nums[l]