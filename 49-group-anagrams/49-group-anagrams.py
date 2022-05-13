class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        lookup = defaultdict(list)
        
        for s in strs:
            key = "".join(sorted(list(s)))
            lookup[key].append(s)
        
        return [l for l in lookup.values()]
        
        
        """
        from collections import Counter
        
        if len(strs)==1 and len(strs[0]) ==0: return [strs]
        
        res = [[strs[0]]]
        for i in range(1,len(strs)):
            for j in range(len(res)):
                if Counter(strs[i]) == Counter(res[j][0]):
                    res[j].append(strs[i])
                    break
                elif j < len(res)-1: continue
                else: res.append([strs[i]])
        
        return res
        """