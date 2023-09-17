class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])

        minHeap = [[0, 0, 0]]  # [diff, r, c]
        visit = set()

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while minHeap:
            diff, r, c = heapq.heappop(minHeap)
            if (r, c) in visit:
                continue

            visit.add((r, c))
            if (r, c) == (ROWS - 1, COLS - 1):
                return diff

            for dr, dc in directions:
                new_row, new_col = r + dr, c + dc
                if (new_row < 0 or new_col < 0 or new_row == ROWS or new_col == COLS or (new_row, new_col) in visit):
                    continue
                new_diff = max(
                    diff, abs(heights[r][c] - heights[new_row][new_col]))
                heapq.heappush(minHeap, [new_diff, new_row, new_col])
