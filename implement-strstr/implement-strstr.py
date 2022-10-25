class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h,window = len(haystack), len(needle)
        for i in range(h-window+1):
            if haystack[i:i+window] == needle: return i 
        return -1