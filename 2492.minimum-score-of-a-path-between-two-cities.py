class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)  # node -> list of (neighbor, dist)
        for src, dst, dist in roads:
            adj[src].append((dst, dist))
            adj[dst].append((src, dist))

        def dfs(i):
            if i in visit:
                return
            visit.add(i)
            nonlocal res
            for neighbor, dist in adj[i]:
                res = min(res, dist)
                dfs(neighbor)

        res = float("inf")
        visit = set()
        dfs(1)
        return res
