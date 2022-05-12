class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
            
        M,N = len(s1), len(s2)
        counterW = Counter(s2[:M-1])
        counterS = Counter(s1)

        for i in range(M-1,N):
            first = i - (M-1)
            counterW[s2[i]] += 1
            if counterW == counterS:
                return True
            counterW[s2[first]] -= 1
            if counterW[s2[first]] == 0:
                counterW.pop(s2[first])

        return False
                