class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        d = {"(": 0, ")": 0}
        unclosed = 0
        for c in s:
            if c == "(":
                d["("] += 1
                unclosed += 1
            elif c == ")":
                if d["("] > 0:
                    d["("] -= 1
                    unclosed -= 1
                else:
                    d[")"] += 1
                    unclosed += 1
        return unclosed