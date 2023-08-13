import sys

sys.setrecursionlimit(10**5)

cache = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
forest = []
n = 0


def dfs(y, x):
    global cache, forest, n
    cache[y][x] = 0

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if forest[y][x] <= forest[ny][nx]:
            continue
        if cache[ny][nx] == -1:
            cache[y][x] = max(cache[y][x], dfs(ny, nx))
        else:
            cache[y][x] = max(cache[y][x], cache[ny][nx] + 1)
    return cache[y][x] + 1


def solution():
    global forest, n, cache
    n = int(input())

    for _ in range(n):
        forest.append(list(map(int, input().split())))
    cache = [[-1] * n for _ in range(n)]
    ans = -1
    for i in range(n):
        for j in range(n):
            if cache[i][j] == -1:
                dfs(i, j)
            ans = max(ans, cache[i][j])
    print(ans + 1)


solution()
