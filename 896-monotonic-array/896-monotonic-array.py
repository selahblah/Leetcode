class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        inc = False
        dec = False
        
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                inc = True
            elif nums[i] > nums[i+1]:
                dec = True
        if inc == True and dec == True:
            return False
        return True
        
        """
        if len(nums) == 1 or 2: return True
        
        if nums[0] <= nums[1]:
            for i in range(2,len(nums)):
                if nums[i-1] > nums[i]: return False
        elif nums[0] >= nums[1]:
            for i in range(2,len(nums)):
                if nums[i-1] < nums[i]: return False
        return True
        """