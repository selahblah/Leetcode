class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        curSum = 0
        prefixSum = {0:1}
        
        for n in nums:
            curSum += n
            diff = curSum - k
            res += prefixSum.get(diff,0)
            prefixSum[curSum] = prefixSum.get(curSum,0) + 1
        return res
        