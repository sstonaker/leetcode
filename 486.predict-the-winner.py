class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = [[-1 for _ in range(n)] for y in range(n)]
        scoreFirst = self.predictTheWinnerInSituation(nums, 0, n - 1, memo)
        scoreTotal = sum(nums)
        return scoreFirst >= scoreTotal - scoreFirst
    
    def predictTheWinnerInSituation(self, nums, i, j, memo):
        # base case
        if i > j:
            return 0
        if i == j:
            return nums[i]
        if memo[i][j] != -1:
            return memo[i][j]
        # recursive
        curScore = max(nums[i] + min(self.predictTheWinnerInSituation(nums, i + 2, j, memo), self.predictTheWinnerInSituation(nums, i + 1, j - 1, memo)), nums[j] + min(self.predictTheWinnerInSituation(nums, i, j - 2, memo), self.predictTheWinnerInSituation(nums, i + 1, j - 1, memo)))
        memo[i][j] = curScore
        return curScore
