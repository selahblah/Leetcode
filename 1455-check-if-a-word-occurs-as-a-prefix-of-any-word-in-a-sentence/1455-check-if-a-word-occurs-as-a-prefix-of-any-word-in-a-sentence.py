class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        sentence = sentence.split()
        l = len(searchWord)
        for i in range(len(sentence)):
            if len(sentence[i])<l: continue
            elif sentence[i][:l] == searchWord: return i+1
        return -1