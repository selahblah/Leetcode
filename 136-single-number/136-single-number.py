class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0 # n ^ 0 = n
        for n in nums:
            res = n ^ res
        return res
    
        """
        res = []
        for n in nums:
            if n in res: res.remove(n)
            else: res.append(n)
        return res[0]
        """