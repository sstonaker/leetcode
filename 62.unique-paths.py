class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
                
        def dfs(r, c, rows, cols, cache):
            if r == rows or c == cols:
                return 0
            if r == rows - 1 or c == cols -1:
                return 1
            if (r, c) in cache:
                 return cache[(r,c)]

            cache[(r, c)] = dfs(r+1, c, rows, cols, cache) + dfs(r, c+1, rows, cols, cache)
            return cache[(r, c)]
        return dfs(0, 0, m, n, {})