class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and nums[0] == target: return 0
        
        l,r = 0,len(nums)-1
        while l<r:
            if target == nums[l]: return l
            elif target == nums[r]: return r
            m = (l+r)//2
            if target == nums[m]: return m
            elif target > nums[m]: l += 1
            else: r -= 1
        return -1