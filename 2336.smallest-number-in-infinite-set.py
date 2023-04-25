import heapq


class SmallestInfiniteSet:

    def __init__(self):
        self.nums = deque(x for x in range(1, 1001))

    def popSmallest(self) -> int:
        if self.nums:
            smallest = self.nums.popleft()
            return smallest
        return -1

    def addBack(self, num: int) -> None:
        if num not in self.nums:
            self.nums.appendleft(num)
            self.nums = deque(sorted(self.nums))


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
