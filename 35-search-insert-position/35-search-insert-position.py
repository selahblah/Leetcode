class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
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