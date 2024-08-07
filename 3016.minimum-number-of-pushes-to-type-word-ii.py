class Solution:
    def minimumPushes(self, word: str) -> int:
        count = {}
        for s in word:
            if s in count:
                count[s] += 1
            else:
                count[s] = 1

        count_arr = []
        for val in count.values():
            count_arr.append(val)
        count_arr.sort(reverse=True)

        pushes = 0
        keys = 0
        for c in count_arr:
            pushes += c * (1 + keys//8)
            keys += 1

        return pushes