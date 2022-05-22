class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def helper(l,r):
            while (l >= 0 and r<len(s) and s[r]==s[l]):
                r += 1
                l -= 1
            return s[l+1:r]
        
        res = ""
        for i in range(len(s)):
            test = helper(i,i)
            if len(res) < len(test) : res = test
            test = helper(i,i+1)
            if len(res) < len(test) : res = test
        
        return res
        
        """
        if len(s) < 2: return s
        
        for i in range(1,len(s)):
            res = ""
            left = i-1
            right = i+1
            while left > -1 and right < len(s) and s[left] == s[right]:
                res = s[left:right+1]
                left -=1
                right += 1
            if (len(res)//2) > (len(s)-i):
                return res
            return res
        """