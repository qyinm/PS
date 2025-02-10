from collections import deque
import sys
input = sys.stdin.readline

def bfs(start, end, graph, N):
    qu = deque()
    visited = [False] * (N + 1)
    qu.append([start, 0])
    visited[start] = True

    while len(qu) > 0:
        curr, cost = qu.popleft()
        if curr == end:
            return cost
        
        for (nxt, ncost) in graph[curr]:
            if visited[nxt]:
                continue
            visited[nxt] = True
            qu.appendleft([nxt, cost + ncost])

def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    
    for _ in range(N - 1):
        a, b, cost = map(int, input().split())
        graph[a].append([b, cost])
        graph[b].append([a, cost])
    
    for _ in range(M):
        start, end = map(int, input().split())
        print(bfs(start, end, graph, N))

if __name__ == "__main__":
    main()