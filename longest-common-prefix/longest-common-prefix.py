class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for word in strs[1:]:
                if i < len(word) and strs[0][i] == word[i]: pass
                else: return res
            res += strs[0][i]
        return res