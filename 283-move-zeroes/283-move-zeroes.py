class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        for i in range(len(nums))[::-1]:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                
                
                