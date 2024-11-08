class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]
        arr.append(-1)


        for i in range(len(arr) - 2, 0, -1):
            arr[i] = max(arr[i], arr[i+1])

        return arr[1:]