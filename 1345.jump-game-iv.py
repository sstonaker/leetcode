class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
        indices = defaultdict(list)
        for i in range(n):
            indices[arr[i]].append(i)
        store_index = deque()
        visited = [False] * n
        store_index.append(0)
        visited[0] = True
        steps = 0

        while store_index:
            size = len(store_index)
            while size > 0:
                current_index = store_index.popleft()
                size -= 1
                if current_index == n - 1:
                    return steps

                jump_next_indices = indices[arr[current_index]]
                jump_next_indices.append(current_index - 1)
                jump_next_indices.append(current_index + 1)
                for jump_next_index in jump_next_indices:
                    if 0 <= jump_next_index < n and not visited[jump_next_index]:
                        store_index.append(jump_next_index)
                        visited[jump_next_index] = True
                jump_next_indices.clear()
            steps += 1
        return -1
