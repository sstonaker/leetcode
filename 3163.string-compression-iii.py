class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        n = len(word)
        
        def prefix(c, i):
            j = 1
            while i + j < n and j < 9:
                if word[i + j] != c:
                    break
                j += 1
            return j
        
        i = 0
        while i < n:
            c = word[i]
            amt = prefix(c, i)
            comp += str(amt)
            comp += word[i]
            i += amt
        return comp
