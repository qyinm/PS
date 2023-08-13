from collections import deque
from copy import deepcopy

ans = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def virus():
    queue = deque()
    newMatrix = deepcopy(matrix)
    for i in range(n):
        for j in range(m):
            if newMatrix[i][j] == 2:
                queue.append((i, j))

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if newMatrix[ny][nx] == 0:
                newMatrix[ny][nx] = 2
                queue.append((ny, nx))
    global ans
    cnt = 0
    for i in range(n):
        cnt += newMatrix[i].count(0)
    ans = max(cnt, ans)


def wall(cnt):
    if cnt == 3:
        virus()
        return
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                matrix[i][j] = 1
                wall(cnt + 1)
                matrix[i][j] = 0


matrix = []
n, m = map(int, input().split())

for _ in range(n):
    matrix.append(list(map(int, input().split())))
wall(0)
print(ans)
