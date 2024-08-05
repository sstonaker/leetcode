class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        kth = 0
        for s in count.items():
            if s[1] == 1:
                kth += 1
                if kth == k:
                    return s[0]
        return ""
