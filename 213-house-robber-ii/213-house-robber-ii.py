class Solution:
    def rob(self, nums: List[int]) -> int:
        
        return max(nums[0], self.cal(nums[1:]), self.cal(nums[:-1]))
        
    def cal(self, nums):
        rob1, rob2 = 0,0
        for n in nums:
            res = max(rob1+n, rob2)
            rob1 = rob2
            rob2 = res
        return rob2
        