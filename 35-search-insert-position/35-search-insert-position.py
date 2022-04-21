class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        left = 0
        right = len(nums)-1
        
        while left <= right:
            mid = (left+right)//2
            if nums[left] < target:
                left += 1
            elif nums[right] > target:
                right -= 1
            else:
                return mid 
        
        return left
                
        
        """
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif target > nums[-1]:
                return len(nums)
            elif target < nums[0]:
                return 0
            else:
                if nums[i-1] < target and target < nums[i]:
                    return i
        """