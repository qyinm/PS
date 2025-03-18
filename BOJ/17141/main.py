from itertools import combinations
from collections import deque
import sys

input = sys.stdin.readline

def spread_virus(board, virus_points, n, blank):
    weight = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    q = deque(virus_points)
    tboard = [[-1] * n for _ in range(n)]
    for y, x, _ in virus_points:
        tboard[y][x] = 0

    fill_cnt = 0
    cnt = 0

    while q:
        cy, cx, cnt = q.popleft()
        fill_cnt += 1

        for wy, wx in weight:
            ny, nx = cy + wy, cx + wx
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue
            if board[ny][nx] == 1 or tboard[ny][nx] != -1:
                continue
            tboard[ny][nx] = cnt + 1
            q.append((ny, nx, cnt+1))
    return cnt if blank == fill_cnt else 1e9

def main():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    virus_points = []
    blank = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                virus_points.append((i, j, 0))
            if board[i][j] != 1:
                blank += 1
    
    points_list = list(combinations(virus_points, m))
    answer = 1e9
    for points in points_list:
        time = spread_virus(board, points, n, blank)
        answer = min(answer, time)
    print(answer if answer != 1e9 else -1)
            

if __name__ == "__main__":
    main()