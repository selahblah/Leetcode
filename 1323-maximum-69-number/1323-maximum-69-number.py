class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        num_ = list(str(num))
        for i in range(len(num_)):
            if num_[i] == '6':
                num_[i] = '9'
                return ''.join(num_)
        return num