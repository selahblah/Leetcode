class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        res,pro = 0,1
        for i in num[::-1]:
            res += pro*i
            pro *= 10
        res += k
        return list(str(res))