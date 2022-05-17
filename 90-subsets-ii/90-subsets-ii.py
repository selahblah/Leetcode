class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = [[]]
        for i in nums:
            res += [j+[i] for j in res]
            
        return [list(l) for l in set([tuple(l) for l in res])]