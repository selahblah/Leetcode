class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        return len(nums) != len(set(nums))
        
        
        
        
        
        
        
        
        
        
        
        
        """
        dic = {}
        for n in nums:
            if n in dic:
                return True
            else:
                dic[n] = 0
        return False
        """
        """        
        return len(nums) != len(set(nums))
        """
           
        """
        for i in range(len(nums)):
            if nums[i] in nums[i+1:]:
                return True
            else:
                pass
        return False
        """
                
                
            