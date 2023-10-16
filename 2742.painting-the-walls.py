class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        dp = {}

        def dfs(i, r):
            if r <= 0:
                return 0
            if i == len(cost):
                return float("inf")
            if (i, r) in dp:
                return dp[(i, r)]

            paint = cost[i] + dfs(i + 1, r - 1 - time[i])
            skip = dfs(i + 1, r)
            dp[(i, r)] = min(paint, skip)
            return dp[(i, r)]

        return dfs(0, len(cost))
