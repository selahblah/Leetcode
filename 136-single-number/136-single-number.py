class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        uniq_nums = list(set(nums))
        count = []
        for i in uniq_nums:
            n = nums.count(i)
            count.append(n)
        for j in count:
            if j == 1:
                return uniq_nums[count.index(1)]