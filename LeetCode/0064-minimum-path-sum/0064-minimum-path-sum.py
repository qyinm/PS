import heapq

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        weight = [(1, 0), (0, 1)]
        n = len(grid)
        m = len(grid[0])
        cost = [[1e9] * m for _ in range(n)]
        pq = []

        cost[0][0] = grid[0][0]
        heapq.heappush(pq, (cost[0][0], 0, 0))

        while pq:
            c, y, x = heapq.heappop(pq)
            
            for wy, wx in weight:
                ny, nx = y + wy, x + wx
                if ny < 0 or ny >= n or nx < 0 or nx >= m:
                    continue
                
                if cost[ny][nx] > grid[ny][nx] + c:
                    cost[ny][nx] = grid[ny][nx] + c
                    heapq.heappush(pq, (cost[ny][nx], ny, nx))
        
        return cost[n-1][m-1]
