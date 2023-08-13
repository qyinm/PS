from collections import deque

dx = [-1, 0, 1, 0]
dy = dx[::-1]

baechu = {}
graph = []

def bfs(graph, x, y, idx):
    queue = deque([[y, x]])
    graph[y][x] = 0
    
    while queue:
        v = queue.popleft()
        for i in range(4):
            nx = v[1] + dx[i]
            ny = v[0] + dy[i]
            if nx <= -1 or nx >= m or ny <= -1 or ny >= n:
                continue
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                queue.append([ny, nx])
c = int(input())
graph = [ [] for x in range(c) ]
baechu = [ 0 for x in range(c) ]
for i in range(c):
    m, n, k = map(int, input().split())
    graph[i] = [ [0] * m for x in range(n) ]
    for j in range(k):
        x, y = map(int, input().split())
        graph[i][y][x] = 1
    for y in range(n):
        for x in range(m):
            if graph[i][y][x] == 1:
                baechu[i] += 1
                bfs(graph[i], x, y, i)

for x in baechu:
    print(x)