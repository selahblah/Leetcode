class Solution:
    def increasingTriplet(self, nums):
        if len(set(nums))<3: return False
        
        n = len(nums)
        first = nums[n-1]
        second = -(2**31)
        
        i = n-2
        while i>=0:
            if nums[i] < second:
                return True
            if first > nums[i]:
                second = nums[i]
            else:
                first = nums[i]
            i -= 1
        return False
        
        """
        s_nums = set(nums)
        if len(s_nums)<3: return False
        
        res = [[nums[0]]]
        for i in range(1,len(nums)):
            for j in range(len(res)):
                if nums[i] > res[j][-1]:
                    res[j].append(nums[i])
                    break
                elif j == len(res)-1: 
                    res.append([nums[i]])
                    
        for li in res:
            if len(li)>=3: return True
        return False
        """
            