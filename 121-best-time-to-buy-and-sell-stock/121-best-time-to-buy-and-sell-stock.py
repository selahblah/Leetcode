class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==1: return 0
        minn, res = prices[0], 0
        
        for sell in prices[1:]:
            res = max(res, sell-minn)
            minn = min(minn,sell)
        return res
            
        
        """
        heap = []
        profit = 0
        
        for price in prices:
            heapq.heappush(heap, price)
            
            if price-heap[0] > profit:
                profit = price-heap[0]
                
        return profit
        """