class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        if len(arr) <= 2:
            return True
        diff = arr[1] - arr[0]
        for i in range(2, len(arr)):
            diff2 = arr[i] - arr[i - 1]
            if diff2 != diff:
                return False
            diff = diff2
        return True
