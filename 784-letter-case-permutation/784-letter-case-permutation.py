class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = [""]
        for c in s:
            tem = []
            if c.isalpha():
                for o in res:
                    tem.append(o+c.lower())
                    tem.append(o+c.upper())
            else:
                for o in res:
                    tem.append(o+c)
            res = tem
        return res