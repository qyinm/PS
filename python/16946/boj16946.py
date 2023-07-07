n, m = map(int, input().split())

Maps = []
for _ in range(n):
    Maps.append(list(map(int, list(input()))))

visited = [[0] * m for _ in range(n)]

zero_queue:list[tuple[int, int]] = []
nozero_set:set[tuple[int, int]] = set()

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]



def bfs(x: int, y: int):
    cnt = 1
    visited[y][x] = 1
    zero_queue.append((x, y))
    nozero_set = set([])
    while len(zero_queue) > 0:
        cx, cy = zero_queue.pop(0)

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if visited[ny][nx] == 1:
                continue
            if Maps[ny][nx] != 0:
                nozero_set.add((nx, ny))
                continue
            
            zero_queue.append((nx, ny))
            visited[ny][nx] = 1
            cnt += 1
    for nozero in nozero_set:
        cx, cy  = nozero
        Maps[cy][cx] += cnt

for i in range(n):
    for j in range(m):
        if Maps[i][j] == 0 and visited[i][j] == 0:
            bfs(j, i)

for Map in Maps:
    for m in Map:
        print(m%10, end="")
    print()