class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy, profit = prices[0], 0
        for i in prices[1:]:
            profit = max(profit, i-buy)
            buy = min(i,buy)
            # if i < buy: buy = i
        return profit
                