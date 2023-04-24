class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while stones:
            if len(stones) == 1:
                return stones[0]
            first_max = stones.pop(stones.index(max(stones)))
            next_max = stones.pop(stones.index(max(stones)))
            if first_max == next_max:
                continue
            else:
                stones.append(first_max - next_max)
        return 0
