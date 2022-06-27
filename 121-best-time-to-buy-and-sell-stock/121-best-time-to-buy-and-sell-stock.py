class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        buy = float("inf")
        for i in prices:
            buy = min(buy,i)
            tem = i-buy
            res = max(res,tem)
        return res