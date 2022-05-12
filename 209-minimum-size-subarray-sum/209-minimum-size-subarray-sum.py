class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        total = 0
        res = float("inf")
        l = 0
        
        for i in range(len(nums)):
            total += nums[i]
            while total >= target:
                total -= nums[l]
                res = min(res, i-l+1)
                l += 1
        
        return 0 if res == float("inf") else res
        """
        for i in range(len(nums)):
            res=[]
            while i < len(nums):
                res.append(nums[i])
                i += 1
                if sum(res)>=target:
                    le = min(le, len(res))
                    continue
                
        return le
        """
        
        