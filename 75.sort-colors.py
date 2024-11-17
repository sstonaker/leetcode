class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = [0, 0, 0]
        for i in range(len(nums)):
            if nums[i] == 0:
                bucket[nums[i]] += 1
            elif nums[i] == 1:
                bucket[nums[i]] += 1
            elif nums[i] == 2:
                bucket[nums[i]] += 1
        
        j = 0
        i = 0
        while i < len(nums):
            while bucket[j] > 0:
                nums[i] = j
                bucket[j] -= 1
                i += 1
            j += 1
        return nums