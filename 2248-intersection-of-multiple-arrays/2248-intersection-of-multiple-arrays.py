class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        res = nums[0]
        for li in nums[1:]:
            res = [value for value in li if value in res]
        res.sort()
        return res