from collections import deque


def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=" ")
    for el in graph[start]:
        if not visited[el]:
            dfs(graph, el, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)




n, m, start = map(int, input().split())
graph = [[] for x in range(n+1)]
dfs_visited = [False] * (n+1)
bfs_visited = [False] * (n+1)
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
for i in range(1, n+1):
    graph[i].sort()

dfs(graph, start, dfs_visited)
print()
bfs(graph, start, bfs_visited)
