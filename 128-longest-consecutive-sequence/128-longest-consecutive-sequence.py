class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for n in nums:
            if n-1 not in nums:
                start = n
                while start in nums:
                    start += 1
                res = max(res,start-n)
        return res