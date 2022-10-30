class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)):
            digits[i] = str(digits[i])
        res = "".join(digits)
        res = str(int(res) + 1)
        return [int(n) for n in res]
        