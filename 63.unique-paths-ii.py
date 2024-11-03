       rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        cache = {}
        def dfs(r, c, rows, cols, cache):
            print(cache)
            if r >= rows or c >= cols:
                return 0
            if obstacleGrid[r][c] == 1:
                return 0
            if r == rows - 1 and c == cols - 1:
                return 1
            if (r, c) in cache:
                return cache[(r, c)]
            
  
            cache[(r, c)] = dfs(r + 1, c, rows, cols, cache) + dfs(r, c + 1, rows, cols, cache)
            print(r, c, cache)
            return cache[(r, c)]
        
        return dfs(0, 0, rows, cols, cache)