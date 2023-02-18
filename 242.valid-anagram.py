class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = {}
        for ch in s:
            if ch in seen:
                seen[ch] += 1
            else:
                seen[ch] = 1
        for ch in t:
            if ch in seen:
                seen[ch] -= 1
                if seen[ch] == 0:
                    del seen[ch]
            else:
                return False
        if seen:
            return False
        return True
