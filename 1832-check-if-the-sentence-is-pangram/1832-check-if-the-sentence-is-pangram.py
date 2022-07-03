class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence)<26: return False
        has = {}
        for i in sentence: has[i] = has.get(i,0) + 1
        return True if len(has) == 26 else False