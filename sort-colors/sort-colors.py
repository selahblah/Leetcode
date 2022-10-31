class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,l,r = 0, 0, len(nums)-1
        while i<=r:
            if nums[i] == 0: 
                nums[i] = nums[l]
                nums[l] = 0 
                l += 1
            elif nums[i] == 2:
                nums[i] = nums[r]
                nums[r] = 2
                r -= 1
                i -= 1
            i += 1
                
                