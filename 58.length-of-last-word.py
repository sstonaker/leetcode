class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = 0
        for c in reversed(s):
            if c == " " and l > 0:
                break
            if c != " ":
                l += 1
        return l