class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = s1.split(" ") + s2.split(" ")
        word_count = {}
        res = []

        for w in words:
            if w in word_count:
                word_count[w] += 1
            else:
                word_count[w] = 1
        for w in word_count:
            if word_count[w] == 1:
                res.append(w)
        return res