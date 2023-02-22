class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        ans = r
        while l <= r:
            mid = (l + r) // 2
            if self.check_weight(weights, days, mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans

    def check_weight(self, weights: List[int], days: int, capacity: int) -> bool:
        required_days = 1
        current_weight = 0
        for weight in weights:
            if current_weight + weight > capacity:
                required_days += 1
                current_weight = 0
            current_weight += weight
        if required_days > days:
            return False
        return True
