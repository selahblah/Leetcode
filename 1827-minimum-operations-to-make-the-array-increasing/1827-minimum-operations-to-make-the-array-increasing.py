class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums)<2: return 0
        res,pre= 0, nums[0]
        for i in nums[1:]:
            if pre>=i:
                pre = pre+1
                res += pre-i
            else: pre = i
        return res