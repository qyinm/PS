from collections import deque

N, M, K, X = map(int, input().split())

q = deque()
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    f, t = map(int, input().split())
    graph[f].append(t)

q.append(X)

visited = [False] * (N + 1)
cnt = 0
visited[X] = True
while len(q) > 0:
    if cnt == K:
        break
    length = len(q)
    for _ in range(length):
        curr = q.popleft()
        
        for nxt in graph[curr]:
            if visited[nxt]:    continue
            visited[nxt] = True
            q.append(nxt)
    cnt += 1

if len(q) == 0:
    print(-1)
else:
    q = list(q)
    q.sort()
    for el in q:
        print(el)
