import math


class Solution:
    def average(self, salary: List[int]) -> float:
        lowest = math.inf
        highest = -math.inf
        total = 0
        for sal in salary:
            if sal < lowest:
                lowest = sal
            if sal > highest:
                highest = sal
            total += sal

        return (total - lowest - highest) / (len(salary) - 2)
