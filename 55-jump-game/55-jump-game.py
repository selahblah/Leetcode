class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest, i, N = 0,0,len(nums)-1
        while i <= farthest and i < N:
            if farthest >= N: break
            farthest = max(farthest, i+nums[i])
            i += 1
        return farthest >= N
            
        """   
        target = len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if i + nums[i] >= target:
                target -= 1
        print(target)
        return True if target == 0 else False
        """