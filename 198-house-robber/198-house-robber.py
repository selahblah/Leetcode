class Solution:
    def rob(self, nums: List[int]) -> int:
        tem1, tem2, res = 0, nums[0], nums[0]
        for n in nums[1:]:
            res = max(tem2,tem1+n)
            tem1 = tem2
            tem2 = res
        return res