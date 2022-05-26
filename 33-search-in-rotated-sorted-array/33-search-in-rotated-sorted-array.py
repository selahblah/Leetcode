class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==1 and nums[0]==target: return 0
        
        l,r = 0, len(nums)-1
        while l<r:
            if nums[l] == target: return l
            elif nums[r] == target: return r
            mid = (r+l)//2
            if nums[mid] == target: return mid
            elif nums[mid] > target: l += 1
            else: r -= 1
                
        return -1
                