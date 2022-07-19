class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = {}
        for n in nums:
            if n in dic.keys(): 
                dic[n] -= 1
                del dic[n]
            else: dic[n] = 1
        return dic.keys()