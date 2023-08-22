import string


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        def int_to_alpha(n: int) -> str:
            i, j = divmod(n, 26)
            if i:
                return int_to_alpha(i - 1) + string.ascii_uppercase[j]
            else:
                return string.ascii_uppercase[j]

        return int_to_alpha(columnNumber - 1)
