class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])

        res = 0
        groups = 0
        i, j = 0, 0

        while i < len(intervals):
            if start[i] <= end[j]:
                groups += 1
                i += 1
            else:
                groups -= 1
                j += 1
            res = max(res, groups)
        return res
