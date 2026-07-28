class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 2:
            return ((nums[0]-1) * (nums[1]-1))

        max1 = 0
        max2 = 0

        for n in nums:
            if n > max1:
                max2 = max1
                max1 = n
            else:
                if n > max2:
                    max2 = n
        
        return ((max1 - 1) * (max2 - 1))
