class Solution:
    def maximumSwap(self, num: int) -> int:
        s = str(num)
        num_arr = [c for c in s]

        max_num = "0"
        max_i = -1
        swap_i, swap_j = -1, -1

        for i in reversed(range(len(num_arr))):
            # max
            if num_arr[i] > max_num:
                max_num = num_arr[i]
                max_i = i
            # swap
            if num_arr[i] < max_num:
                swap_i = i
                swap_j = max_i

        num_arr[swap_i], num_arr[swap_j] = num_arr[swap_j], num_arr[swap_i]
        
        return int("".join(num_arr))