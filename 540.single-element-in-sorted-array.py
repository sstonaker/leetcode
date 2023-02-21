class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            # the array will be an odd number
            # the single element will be in the odd length
            a = mid % 2 == 0 and nums[mid] == nums[mid - 1]
            b = mid % 2 != 0 and nums[mid] == nums[mid + 1]
            if a or b:
                r = mid - 1
            else:
                l = mid + 1
        return nums[l - 1]
