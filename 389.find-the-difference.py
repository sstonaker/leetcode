class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        chars = {}
        for c in t:
            if c in chars:
                chars[c] += 1
            else:
                chars[c] = 1
        for c in s:
            if c in chars:
                chars[c] -= 1
                if chars[c] == 0:
                    del chars[c]
        missing = list(chars.keys())[0]
        return missing
