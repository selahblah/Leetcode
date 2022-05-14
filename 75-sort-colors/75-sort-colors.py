class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def switch(j, s):
            tem = nums[j]
            nums[j] = nums[s]
            nums[s] = tem
            
        left = 0
        right = len(nums)-1
        
        i = 0
        while i <= right:
            if nums[i] == 0:
                switch(left,i)
                left += 1
            elif nums[i] == 2:
                switch(right,i)
                right -= 1
                i -= 1 
            i += 1
        