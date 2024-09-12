class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        res = 0

        for w in words:
            temp = 0
            for c in w:
                if c in allowed:
                    temp += 1
                else:
                    break
            if temp == len(w):
                res += 1
        return res

        