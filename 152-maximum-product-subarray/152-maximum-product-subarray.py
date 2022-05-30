class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<1: return 0
        curmax = curmin = maxx = nums[0]
        
        for n in nums[1:]:
            temmax = curmax
            curmax = max(curmax*n,curmin*n,n)
            curmin = min(temmax*n,curmin*n,n)
            maxx = max(curmax, maxx)
        
        return maxx
        
        """
        N = len(nums)
        if N<1: return 0
        dp_max = dp_min = [0]*N
        dp_max[0] = dp_min[0] = nums[0]
        
        for i in range(1,N):
            if nums[i] > 0:
                dp_max[i] = max(dp_max[i-1]*nums[i],nums[i])
                dp_min[i] = min(dp_min[i-1]*nums[i],nums[i])
            else:
                dp_max[i] = max(dp_min[i-1]*nums[i],nums[i])
                dp_min[i] = min(dp_max[i-1]*nums[i],nums[i])
            print(dp_max,dp_min)
                
        return max(dp_max)
        """