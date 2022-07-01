class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        res1,res2 = Counter(word1), Counter(word2) 
        
        for i in res1:
            if i in res2: res2[i] = abs(res2[i]-res1[i])
            else: res2[i] = res1[i]
        
        for i in res2.values(): 
            if i>3: return False
        return True
                