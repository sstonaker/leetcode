class Solution:
    def climbStairs(self, n: int) -> int:
        # one = 1
        # two = 1

        # for i in range(n-1):
        #     temp = one
        #     one = one + two
        #     two = temp
        
        # return one

        def dfs(step, cache):
            if step == n:
                return 1
            if step > n:
                return 0
            if step in cache:
                return cache[step]
            
            cache[step] = dfs(step + 1, cache) + dfs(step + 2, cache)
            return cache[step]
        return dfs(0, {})