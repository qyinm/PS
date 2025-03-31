import heapq
import sys
input = sys.stdin.readline

INF = float('inf')
weight = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dijkstra(n, matrix):
    cost = [[INF] * n for _ in range(n)]
    cost[0][0] = matrix[0][0]
    hq = [(cost[0][0], 0, 0)]    # cost, y, x

    while hq:
        cur_cost, cur_y, cur_x = heapq.heappop(hq)

        if cur_y == n - 1 and cur_x == n - 1:
            return cur_cost
        
        for wy, wx in weight:
            next_y, next_x = cur_y + wy, cur_x + wx

            if next_y < 0 or next_y >= n or next_x < 0 or next_x >= n:
                continue

            if cur_cost + matrix[next_y][next_x] < cost[next_y][next_x]:
                cost[next_y][next_x] = cur_cost + matrix[next_y][next_x]
                heapq.heappush(hq, (cost[next_y][next_x], next_y, next_x))

def main():
    cycle = 1
    while True:
        n = int(input())
        if n == 0:
            break

        matrix = [list(map(int, input().split())) for _ in range(n)]

        print(f'Problem {cycle}: {dijkstra(n, matrix)}')
        cycle += 1

if __name__ == "__main__":
    main()