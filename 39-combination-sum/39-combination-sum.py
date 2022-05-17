class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        res = [[] for i in range(target+1)]
        
        for c in candidates:
            for t in range(1,target+1):
                if c > t: continue
                if c == t: res[t].append([c])
                for x in res[t-c]:
                    res[t].append(x+[c])
        return res[-1]
                    