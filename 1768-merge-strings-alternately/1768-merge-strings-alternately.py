class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        word1, word2 = deque(word1), deque(word2)
        i, j = len(word1), len(word2)
        res = ""
        while i>0 or j>0:
            if i>0:
                res += word1.popleft()
                i -= 1
            if j>0:
                res += word2.popleft()
                j -= 1
        return res