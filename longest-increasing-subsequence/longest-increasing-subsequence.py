class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tem = [nums[0]]
        for n in nums:
            x = bisect_left(tem,n)
            if x == len(tem): tem.append(n)
            elif tem[x] > n: tem[x] = n
        return len(tem)