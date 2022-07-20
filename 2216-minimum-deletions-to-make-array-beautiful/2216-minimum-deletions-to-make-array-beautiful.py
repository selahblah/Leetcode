class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            if (i+res-1)%2==0 and nums[i-1]==nums[i]: res += 1
                
        if (len(nums)-res)%2 == 1: res += 1
        return res