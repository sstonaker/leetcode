class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1set, nums2set = set(nums1), set(nums2)
        res1, res2 = set(), set()
        for num in nums1:
            if num not in nums2set:
                res1.add(num)
        for num in nums2:
            if num not in nums1set:
                res2.add(num)

        return [list(res1), list(res2)]
