class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        
        for i in range(1, len(dp)):
            for c in coins:
                if i-c >= 0: 
                    dp[i] = min(dp[i], dp[i-c]+1)
                    
        return -1 if dp[-1]==float('inf') else dp[-1]
        
        
        """
        if not amount: return 0
        coins.sort()
        count, tem = 0, 0
        
        for i in range(len(coins)-1,-1,-1):
            if tem + coins[i] > amount: continue
            while i >= 0 and tem <= amount:
                tem += coins[i]
                count += 1
            tem -= coins[i]
            count -= 1
        
        if tem == amount: return count
        else: return -1
        """