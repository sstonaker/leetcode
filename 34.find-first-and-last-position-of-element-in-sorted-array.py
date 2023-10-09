class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        for i in range(len(nums)):
            if nums[i] == target:
                res[0] = i
                break
        for i in range(len(nums) - 1, -1, -1):
            print(i)
            if nums[i] == target:
                res[1] = i
                break
        return res
