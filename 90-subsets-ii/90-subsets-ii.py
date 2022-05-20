class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = [[]]
        for i in nums:
            res += [[i]+j for j in res]
        return [list(r) for r in set(tuple(l) for l in res)]