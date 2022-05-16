class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = defaultdict(list)
        
        for s in strs:
            key = "".join(sorted(s))
            dic[key].append(s)
        
        return [l for l in dic.values()]