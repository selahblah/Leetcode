class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        """
        O(logn) time.......
        No max
        No >
        """
        
        left = 0
        right = len(nums)-1
        
        while left < right:
            mid = left + (right-left)//2
            if nums[mid] < nums[mid+1]:
                left = mid+1
            else:
                right = mid
        return left
        
        """
        left = 0
        right = len(nums)-1
        
        while left < right:
            mid = (left+right)//2
            if nums[mid] > nums[mid+1]:
                right = mid
            else: 
                left = mid +1
        return left
        """