class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj = defaultdict(list)
        for src, dst in relations:
            adj[src].append(dst)

        max_time = {}  # src -> max_time

        def dfs(src):
            if src in max_time:
                return max_time[src]

            res = time[src - 1]
            for neighbor in adj[src]:
                res = max(res, time[src - 1] + dfs(neighbor))
            max_time[src] = res
            return res

        for i in range(1, n + 1):
            dfs(i)

        return max(max_time.values())
