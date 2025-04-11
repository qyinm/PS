from collections import deque
import sys

input = sys.stdin.readline

def main():
    n, m, r = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    for g in graph:
        g.sort(reverse=True)

    visited = [False] * (n + 1)
    visited[r] = True
    queue = deque([r])
    
    orders = [0] * (n + 1)
    order = 1
    while queue:
        v = queue.popleft()
        orders[v] = order
        order += 1

        for u in graph[v]:
            if not visited[u]:
                visited[u] = True
                queue.append(u)
    
    for i in range(1, n + 1):
        print(orders[i])


if __name__ == "__main__":
    main()
