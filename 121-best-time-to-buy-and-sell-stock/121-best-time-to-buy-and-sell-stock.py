class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        heap = []
        profit = 0
        
        for price in prices:
            heapq.heappush(heap, price)
            
            if price-heap[0] > profit:
                profit = price-heap[0]
                
        return profit