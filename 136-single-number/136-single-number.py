class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dic = {}
        
        for i in nums:
            if i not in dic: 
                dic[i]=i
            else:
                del dic[i]
        
        for i in dic:
            return i
        
        """
        uniq_nums = list(set(nums))
        count = []
        for i in uniq_nums:
            n = nums.count(i)
            count.append(n)
        
        return uniq_nums[count.index(1)]
        """