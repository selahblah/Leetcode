class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        count = Counter(nums)
        for i in count.values():
            if i>1: res += comb(i,2)
        return res
            