class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right, left = 0, sum(nums)
        for i in range(len(nums)):
            if right == left-nums[i]: return i
            right += nums[i]
            left -= nums[i] 
        """
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]): return i
        """
        return -1