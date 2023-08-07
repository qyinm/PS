m, n = 0, 0
matrix = []
cache = []


dx = [1, 0, -1, 0]
dy = [0, -1, 0 , 1]

cnt = 0

def dfs(y, x):
    global cnt, cache, matrix
    cache[y][x] = 0

    if y == m-1 and x == n-1:
        cache[y][x] = 1
        return cache[y][x]
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if cache[ny][nx] == 0:
            continue
        if matrix[y][x] <= matrix[ny][nx]:  continue
            
        if cache[ny][nx] >= 0:
            cache[y][x] += cache[ny][nx]
        else:   cache[y][x] += dfs(ny, nx)
    return cache[y][x]

def solution():
    global m, n, matrix, cache
    m, n = map(int, input().split())
    
    cache = [[-1] * n for _ in range(m)]
    for _ in range(m):
        matrix.append(list(map(int, input().split())))
    dfs(0, 0)
    print(cache[0][0])

solution()
