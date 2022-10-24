class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,j,n = 0,0,len(nums)
        while j < n:
            if nums[i] == 0: 
                nums.pop(i)
                nums.append(0)
                i -= 1
            i += 1
            j += 1