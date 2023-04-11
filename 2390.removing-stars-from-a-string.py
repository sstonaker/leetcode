class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch is not "*":
                stack.append(ch)
            else:
                stack.pop()
        return "".join(stack)
