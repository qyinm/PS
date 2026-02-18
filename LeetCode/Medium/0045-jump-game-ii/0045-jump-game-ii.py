import heapq

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0

        pq = [(0, 0, -nums[0])]
        visited = set({0})

        while pq:
            jump, curr, jump_power = heapq.heappop(pq)
            start, end = curr, curr - jump_power + 1

            if end >= n:
                return jump + 1
            for idx in range(start + 1, end):
                if idx in visited:
                    continue
                
                heapq.heappush(pq, (jump + 1, idx, -nums[idx]))
                visited.add(idx)
