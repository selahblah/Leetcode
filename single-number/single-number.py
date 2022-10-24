class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = [nums[0]]
        
        for n in nums[1:]:
            if n not in res: res.append(n)
            else: res.remove(n)
        return res[0]