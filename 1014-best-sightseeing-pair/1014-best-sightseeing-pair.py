class Solution(object):
    def maxScoreSightseeingPair(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        
        res = float("-inf")
        aii = values[0]+0
        
        for j in range(1,len(values)):
            res = max(res, aii+values[j]-j)
            aii = max(aii,values[j]+j)
            
        return res
            
        """
        res = float("-inf")
        for i in range(len(values)-1):
            for j in range(i+1,len(values)):
                tem = values[i] + values[j] + i - j
                res = max(res,tem)
        return res
        """
        
        """
        res = float("-inf")
        l,r = 0, len(values)-1
        while l<r:
            tem = values[l]+values[r]+l-r
            res = max(res,tem)
            if values[l]>values[r]: r -= 1
            else: l += 1
        return res
        """