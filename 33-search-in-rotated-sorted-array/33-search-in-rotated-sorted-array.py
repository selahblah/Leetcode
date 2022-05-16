class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==1 and nums[0]==target: return 0
        
        left = 0
        right = len(nums)-1
        
        while left < right:
            if nums[left] == target: return left
            elif nums[right] == target: return right
            mid = (left + right)//2
            if nums[mid] == target: return mid
            elif nums[mid]> target:
                right -= 1
            else: left += 1
        
        return -1