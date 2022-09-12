class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        l,r = 0, len(nums)-1
        while l < r:
            m = l + (r-l)//2
            if nums[m] > nums[m+1]: return nums[m+1]
            elif nums[l] > nums[r]: l += 1
            else: return nums[l]
        return nums[l]
        
        """
        l,r = 0,len(nums)-1
        while l < r:
            m = l+(r-l)//2
            if nums[m] > nums[m+1]: return nums[m+1]
            elif nums[l] < nums[r]: return nums[l]
            elif nums[l] < nums[m] and nums[r] < nums[m]: l += 1
            else: r -= 1
        """
            
            