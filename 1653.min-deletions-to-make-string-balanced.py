class Solution:
    def minimumDeletions(self, s: str) -> int:
        res = 0
        b = 0
        for c in s:
            if c == 'a':
                res = min(res + 1, b)
            else:
                b += 1
        return res