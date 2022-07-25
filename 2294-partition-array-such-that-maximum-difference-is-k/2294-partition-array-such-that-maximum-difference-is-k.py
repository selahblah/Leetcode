class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        
        c = collections.Counter(nums)
        inf = 10**20
        res = 0
        last = -inf
        key = sorted(c.keys())
        for n in key:
            if abs(n-last)>k:
                last = n
                res += 1
        return res
        
        """
        nums.sort()
        res, i = 0, 1
        tem = [nums[0]]
        while i < len(nums):
            while i < len(nums) and tem[-1]-tem[0] <= k:
                tem.append(nums[i])
                i += 1
            i += 1
            res += 1
            if i<len(nums): tem = [nums[i]]
        return res
        """