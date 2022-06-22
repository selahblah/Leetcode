class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            while (r-l+1) - max(count.values())> k:
                count[s[l]] -= 1
                l += 1
            res = max(res,r-l+1)
        return res
        
        """
        res2,i = 1,0
        while i < len(s)-k:
            tem, count, res = s[i], 0, 1
            while i < len(s)-1 and count <= k:
                if count == k and tem != s[i+1]: break
                elif tem != s[i+1]: count += 1
                i += 1
                res += 1
            i += 1
            res2 = max(res2, res)
        return res2
        """