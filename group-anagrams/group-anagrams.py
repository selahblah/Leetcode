class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
            dic[key].append(word)
        return dic.values()