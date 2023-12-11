from collections import deque

def bfs(adj, vis, start):
    queue = deque([])
    queue.append(start)
    vis[start] = 0
    while queue:
        cur = queue.popleft()
        for nxt in adj[cur]:
            if vis[nxt] != -1:
                continue
            vis[nxt] = vis[cur] + 1
            queue.append(nxt)
    
    return vis

def main():
    n, m = map(int, input().split())
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    minsum = float('inf')
    minidx = -1
    for i in range(1, n + 1):
        vis = [-1 for _ in range(n + 1)]
        result = sum(bfs(adj, vis, i))
        # print(f'result: {result}')
        if result < minsum:
            minsum = result
            minidx = i
    print(minidx)
    
if __name__ == "__main__":
    main()
