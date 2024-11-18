class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0] * n
        if k == 0:
            return res
        
        
        # for i in range(n):
        #     if k > 0:
        #         for j in range(i+1, i+1+k):
        #             res[i] += code[j % n]
        #     if k < 0:
        #         for j in range(i-1, i-1-abs(k), -1):
        #             res[i] += code[j % n]
        
        # return res

        l = 0
        cur_sum = 0

        for r in range(n + abs(k)):
            cur_sum += code[r % n]

            if r - l + 1 > abs(k):
                cur_sum -= code[l % n]
                l = (l + 1) % n
            if r - l + 1 == abs(k):
                if k > 0:
                    res[(l - 1) % n] = cur_sum
                elif k < 0:
                    res[(r + 1) % n] = cur_sum
        return res
            
        
        return res