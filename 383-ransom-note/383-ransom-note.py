class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        maga = list(magazine)
        
        for i in ransomNote:
            if i in maga:
                maga.remove(i)
            else:
                return False
                
        return True