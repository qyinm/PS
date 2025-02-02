from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

link = {}
for _ in range(m):
    sy, sx, ey, ex = map(int, input().split())
    start = (sy, sx)
    end = (ey, ex)
    
    if not start in link:
        link[start] = []
    link[start].append(end)

weight = [(0, 1), (0, -1), (1, 0), (-1, 0)]
qu = deque()

board = [[False] * (n + 1) for _ in range(n + 1)]
board[1][1] = True
visited = [[False] * (n + 1) for _ in range(n + 1)]
visited[1][1] = True

answer = 1
while True:
    flag = True
    qu.append((1, 1))
    while len(qu) > 0:
        curr = qu.popleft()
        if curr in link:
            for (room_y, room_x) in link[curr]:
                if board[room_y][room_x]:
                    continue
                board[room_y][room_x] = True
                answer += 1
                flag = False
        
        for (wy, wx) in weight:
            ny = curr[0] + wy
            nx = curr[1] + wx
            if (ny < 1 or ny > n or nx < 1 or nx > n):   continue
            if not board[ny][nx] or visited[ny][nx]:    continue
            visited[ny][nx] = True
            qu.append((ny, nx))
    if flag:
        break

print(answer)