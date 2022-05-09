class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if not nums: return -1
        if len(nums)==1 : return nums[0]
        
        left = 0
        right = len(nums)-1
        
        while left < right:
            mid = left + (right-left)//2
            if mid > 0 and nums[mid] < nums[mid-1]:
                return nums[mid]
            elif nums[left] <= nums[mid] and nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid-1
                
        return nums[left]