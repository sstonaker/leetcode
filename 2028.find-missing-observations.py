class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        num_rolls = len(rolls) + n
        missing_sum = mean * num_rolls - sum(rolls)
        if missing_sum / n < 1 or missing_sum / n > 6:
            return []
        res = []
        for i in range(n):
            missing = min(6, missing_sum - n + 1)
            n -= 1
            missing_sum -= missing
            res.append(missing)
        return res