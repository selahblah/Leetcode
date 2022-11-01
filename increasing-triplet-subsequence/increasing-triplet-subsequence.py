class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        tem = [nums[0]]
        for n in nums[1:]:
            x = bisect_left(tem,n)
            if x == len(tem): tem.append(n)
            elif x < len(tem): tem[x] = n
            if len(tem) == 3: return True 
        return False