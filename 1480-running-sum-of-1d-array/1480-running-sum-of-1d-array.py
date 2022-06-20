class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        tem, res = 0, []
        for i in nums:
            tem += i
            res.append(tem)
        return res
        """
        res = [0]
        for i in nums:
            res.append(res[-1]+i)
        return res[1:]
        """