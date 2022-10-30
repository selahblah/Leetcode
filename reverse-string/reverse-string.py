class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l,r = 0,len(s)-1
        while l < r:
            tem = s[r]
            s[r] = s[l]
            s[l] = tem
            l += 1
            r -= 1