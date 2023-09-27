class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0
        i = 0

        for c in s:
            if c.isdigit():
                size *= int(c)
            else:
                size += 1
            i += 1

        for j in range(i - 1, -1, -1):
            c = s[j]
            if c.isdigit():
                size = size // int(c)
                k %= size
            else:
                if (k == 0 or k == size):
                    return c
                size -= 1
