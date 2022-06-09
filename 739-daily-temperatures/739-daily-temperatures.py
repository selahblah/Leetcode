class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res = [[i,0] for i in range(len(temperatures))]
        has = [[-1,temperatures[0]]]
        for i,j in enumerate(temperatures[1:]):
            while has and j > has[-1][1]:
                res[has[-1][0]+1][1] = i-has[-1][0]
                has.pop()
            has.append([i,j])
        
        return [i[1] for i in res]