class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        target = len(nums)-1
        for n in range(len(nums)-1,-1,-1):
            if n + nums[n] >= target:
                target = n
            
        return True if target ==0 else False
        