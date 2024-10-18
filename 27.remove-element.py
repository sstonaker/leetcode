class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        last = len(nums) - 1
        while l < len(nums):
            if last < l:
                break
            if nums[l] == val:
                if nums[last] != val:
                    nums[l] = nums[last]
                    l += 1
                    last -= 1
                else:
                    last -= 1
            else:
                l += 1
        return l