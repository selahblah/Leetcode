class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted(stones)
        while len(stones)>1:
            stones = sorted(stones)
            tem = stones[-1]-stones[-2]
            if tem == 0:
                stones = stones[:-2]
            else:
                stones.pop()
                stones[-1] = tem
                
        return 0 if not stones else stones[0]