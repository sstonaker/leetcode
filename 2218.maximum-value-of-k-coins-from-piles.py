class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        dp = [[-1] * (k + 1) for _ in range(n)]

        def dfs(i, coins):
            if i == n:
                return 0
            if dp[i][coins] != -1:
                return dp[i][coins]

            dp[i][coins] = dfs(i + 1, coins)  # skip current pile
            current_pile = 0
            for j in range(min(coins, len(piles[i]))):
                current_pile += piles[i][j]
                dp[i][coins] = max(
                    dp[i][coins], current_pile + dfs(i+1, coins - j - 1))
            return dp[i][coins]
        return dfs(0, k)
