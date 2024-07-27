class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = [0]
        for i in range(len(nums)):
            running_sum.append(running_sum[i] + nums[i])
        return running_sum[1:]