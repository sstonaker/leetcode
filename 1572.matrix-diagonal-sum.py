class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res, n = 0, len(mat)

        for i in range(n):
            res += mat[i][i]  # primary diagonal
            res += mat[i][n - 1 - i]  # secondary diagonal

        return res - (mat[n // 2][n // 2] if n % 2 else 0)
