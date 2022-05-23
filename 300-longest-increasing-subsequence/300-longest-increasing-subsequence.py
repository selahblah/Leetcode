class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        """
        tem = [nums[0]]
        
        for n in nums:
            x = bisect_left(tem,n)
            if x == len(tem): tem.append(n)
            elif tem[x] > n: tem[x] = n
        
        return len(tem)
        
        
        """
        N = len(nums)
        dp = [1]*N
        
        for n in range(len(nums)):
            for i in range(n):
                if nums[n] > nums[i]:
                    dp[n] = max(dp[n],dp[i]+1)
        return max(dp)
        """

        """
        if len(nums)==1: return 1
        
        res, i = 0, 0
        
        for i in range(len(nums)-1):
            has = [nums[i]]
            j = i + 1
            while j < len(nums):
                if has[-1] < nums[j]:
                    has.append(nums[j])
                    j += 1
                elif len(has) > 1 and has[-2] < nums[j] < has[-1]:
                    has.pop()
                    has.append(nums[j])
                    j += 1
                else:
                    j += 1
                    continue
            i += 1
            res = max(res, len(has))      
        return res
        """
                    