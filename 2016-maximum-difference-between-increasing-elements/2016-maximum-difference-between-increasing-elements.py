class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        minn, res = float("inf"),0
        for i in nums:
            minn = min(minn,i)
            res = max(res,i-minn)
        return -1 if res == 0 else res 
            