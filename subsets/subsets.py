class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = [[]]
        for n in nums:
            res += [[n]+j for j in res]
        return res
        
    
        
        """
        # sol1
        res = [[]]
        for n in nums:
            for li in res:
                res.append(li.append(n))
        return res
        
        # sol2
        res = [[]]
        for n in nums:
            res += [j +[n] for j in res]
        return res
        """
        