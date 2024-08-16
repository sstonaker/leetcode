class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res = 0
        cur_min = arrays[0][0]
        cur_max = arrays[0][-1]
        for arr in arrays[1:]:
            dist1 = abs(cur_max - arr[0])
            dist2 = abs(cur_min - arr[-1])
            res = max(res, dist1, dist2)
            cur_min = min(cur_min, arr[0])
            cur_max = max(cur_max, arr[-1])
        return res