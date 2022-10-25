class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = len(s)-1
        while i > -1:
            s.insert(len(s)-1-i,s[-1])
            i -= 1
            s.pop()