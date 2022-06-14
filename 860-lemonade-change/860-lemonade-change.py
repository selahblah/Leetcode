class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        wallet = {5:0, 10:0, 20:0}
        for b in bills:
            if b == 5: wallet[5] += 1
            elif b == 10:
                if wallet[5] == 0: return False
                wallet[10] += 1
                wallet[5] -= 1
            else:
                if wallet[10] > 0 and wallet[5] > 0:
                    wallet[10] -= 1
                    wallet[5] -= 1
                elif wallet[5] >= 3: wallet[5] -= 3
                else: return False
                    
        return True
                