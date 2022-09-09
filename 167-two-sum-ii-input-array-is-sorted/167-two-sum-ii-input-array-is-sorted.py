class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(numbers)):
            a = target-numbers[i]
            if a in numbers[i+1:]:
                j = numbers[i+1:].index(a)
                return [i+1, i+j+2]