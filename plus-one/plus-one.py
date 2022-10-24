class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = int("".join([str(n) for n in digits]))+1
        return [int(d) for d in str(digits)]