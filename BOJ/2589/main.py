import sys
from collections import deque
input = sys.stdin.readline


def find_shortest_path(graph, n, m, start_y, start_x):
    
    path_count = [[-1] * m for _ in range(n)]
    path_count[start_y][start_x] = 0
    max_path_distance = -1
    queue = deque([(start_y, start_x)])
    while queue:
        y, x = queue.popleft()
        for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ny, nx = y + dy, x + dx
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if graph[ny][nx] == 'W' or path_count[ny][nx] != -1:
                continue
            path_count[ny][nx] = path_count[y][x] + 1
            queue.append((ny, nx))

            if max_path_distance < path_count[ny][nx]:
                max_path_distance = path_count[ny][nx]

    return max_path_distance

def main():
    n, m = map(int, input().split())
    graph = [list(input().strip()) for _ in range(n)]
    max_path_distance = -1
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'L':
                max_path_distance = max(max_path_distance, find_shortest_path(graph, n, m, i, j))

    print(max_path_distance)

if __name__ == "__main__":
    main()