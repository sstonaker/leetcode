class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        cols = len(grid[0])
        rows = len(grid)
        count = 0
        for i in range(rows - 1, -1, -1):
            if grid[i][-1] >= 0:
                break
            for j in range(cols - 1, -1, -1):
                if grid[i][j] < 0:
                    count += 1
                if grid[i][j] >= 0:
                    break
        return count
