class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        totalword = {}
        for c in words2:
            tem = Counter(c)
            for k,v in tem.items():
                if k not in totalword:
                    totalword[k] = v
                else:
                    totalword[k] = max(v,totalword[k])
        res = []
        for w in words1:
            tem = Counter(w)
            if all([k in tem and v<=tem[k] for k,v in totalword.items()]):
                res.append(w)
        return res