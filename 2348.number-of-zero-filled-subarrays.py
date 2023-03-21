class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count, result = 0, 0
        for num in nums:
            if num == 0:
                count += 1
                result += count
            else:
                count = 0
        return result
