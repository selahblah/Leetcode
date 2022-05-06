class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter 
        
        a = Counter(nums)
        key = a.keys()
        val = a.values()
        
        return key[val.index(max(val))]