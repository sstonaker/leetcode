class Solution:
    def countOrders(self, n: int) -> int:
        # 2*n slots
        # count valid ways to array a pair p1, d1
        # x * (x - 1) = choices
        # x * (x - 1) / 2 = valid choices

        slots = 2 * n
        output = 1
        while slots > 0:
            valid_choices = slots * (slots - 1) // 2
            output *= valid_choices
            slots -= 2
        return output % (10**9 + 7)
