class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        prev_row = [poured]  # flow

        for row in range(1, query_row + 1):
            cur_row = [0] * (row + 1)
            for i in range(row):
                extra = prev_row[i] - 1
                if extra > 0:
                    cur_row[i] += .5 * extra
                    cur_row[i + 1] += .5 * extra
            prev_row = cur_row

        return min(1, prev_row[query_glass])
