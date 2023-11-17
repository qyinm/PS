import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(start):
    global graph
    vis = [False for _ in range(n+1)]
    vis[start] = True    
    q = deque([start])
    
    cnt = 1
    while q:
        top = q.popleft()
        for i in graph[top]:
            if vis[i]:
                continue
            vis[i] = True
            q.append(i)
            cnt += 1
    return cnt
    
ans = []
mm = 1

for i in range(1, n+1):

    ret = bfs(i)

    if ret > mm:
        ans.clear()
        ans.append(i)
        mm = ret
    elif ret == mm:
        ans.append(i)
print(*ans)
