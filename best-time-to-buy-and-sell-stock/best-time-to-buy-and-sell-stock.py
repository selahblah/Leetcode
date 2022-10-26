class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        buy = prices[0]
        for s in prices[1:]:
            buy = min(buy,s)
            profit = max(profit, s-buy)
        return profit