class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0,len(numbers)-1
        while l<r:
            s = numbers[l]+numbers[r]
            if s > target: r -= 1
            elif s < target: l += 1
            else: return [l+1,r+1]
        
        """
        res = []
        for i in range(len(numbers)):
            a = target-numbers[i]
            if a in numbers[i+1:]:
                j = numbers[i+1:].index(a)
                return [i+1, i+j+2]
        """