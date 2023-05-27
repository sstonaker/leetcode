class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = {}

        # return num of stones alice gets
        def dfs(alice, i, M):
            if i == len(piles):
                return 0
            if (alice, i, M) in dp:
                return dp[(alice, i, M)]

            res = 0 if alice else float("inf")
            total = 0
            for x in range(1, 2 * M + 1):
                if i + x > len(piles):
                    break
                total += piles[i + x - 1]
                if alice:
                    res = max(res, total + dfs(not alice, i + x, max(x, M)))
                else:
                    res = min(res, dfs(not alice, i + x, max(x, M)))
            dp[(alice, i, M)] = res
            return res
        return dfs(True, 0, 1)
