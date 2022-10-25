class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        l,r = 0,len(s)-1
        while l<r:
            s[l],s[r] = s[r],s[l]
            l += 1
            r -= 1
        
        """
        i = len(s)-1
        while i > -1:
            s.insert(len(s)-1-i,s[-1])
            i -= 1
            s.pop()
        """