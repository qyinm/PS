from collections import deque

dx = [-1, 0, 1, 0]
dy = dx[::-1]

n, m = map(int, input().split())
graph = []
visited = [ [False] * m for i in range(n) ]
for i in range(n):
    temp = list(map(int, input()))
    graph.append(temp)

def bfs():
    queue = deque([[0, 0]])

    while queue:
        v = queue.popleft()

        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]

            if nx <= -1 or nx >= m or ny <= -1 or ny >= n:
                continue

            if graph[ny][nx] != 0 and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append([nx, ny])
                graph[ny][nx] += graph[v[1]][v[0]]
    
    print(graph[n-1][m-1])

bfs()