class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums)==1 and nums[0]==target: return True
        elif len(nums)==1: return False
        
        l,r = 0,len(nums)-1
        while l<r:
            mid = l+(r-l)//2
            if (nums[mid] == target) or (nums[l] == target) or (nums[r] == target): return True
            elif nums[l]<target: l += 1
            else: r -= 1
        return False
        """
        for i in nums:
            if i == target: return True
        return False
        """