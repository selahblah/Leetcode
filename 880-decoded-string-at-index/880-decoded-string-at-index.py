class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        size = 0
        for i, c in enumerate(S):
            if c.isdigit():
                size *= int(c)
            else:
                size += 1
            if K <= size:
                break
        for c in S[i::-1]:
            if c.isdigit():
                size /= int(c)
                K %= size
            else:
                if K % size == 0:
                    return c
                size -= 1
        """
        res = ""
        i = 0
        while i < len(s):
            while i < len(s) and s[i].isalpha():
                res += s[i]
                i += 1
            if i < len(s) and s[i].isdigit(): res *= int(s[i])
            i += 1
            if len(res) >= k: return res[k-1]
        """