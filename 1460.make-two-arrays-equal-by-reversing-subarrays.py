class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        count = defaultdict(int)

        for i, j in zip(target, arr):
            count[i] += 1
            count[j] -= 1
        
        for n in count:
            if count[n] != 0:
                return False
        return True