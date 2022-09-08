class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy, res = float("inf"), 0
        for i in prices:
            buy = min(i,buy)
            res = max(res,i-buy)
        return res