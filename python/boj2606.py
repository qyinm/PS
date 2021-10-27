from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    virusNum = 0
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                virusNum +=1
    return virusNum

comCount = int(input())
nodeCount = int(input())
graph = [[] for i in range(comCount+1)]
visited = [False] * (comCount+1)
for i in range(nodeCount):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
for i in range(1, comCount):
    graph[i].sort()

print(bfs(graph, 1, visited))
