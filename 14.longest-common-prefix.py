class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""


        shortest = strs[0]

        for s in strs:
            if len(s) < len(shortest):
                shortest = s

        for i in range(len(shortest)):
            for s in strs:
                if s[i] != shortest[i]:
                    return res
            res += s[i]

        return res