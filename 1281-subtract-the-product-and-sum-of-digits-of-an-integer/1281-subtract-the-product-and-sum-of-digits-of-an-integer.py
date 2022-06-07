class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        plus, pro = 0, 1
        for i in list(str(n)):
            plus += int(i)
            pro *= int(i)
        return pro-plus