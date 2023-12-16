from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(row, col, graph, n, m):
    queue = deque([])
    queue.append([row, col])
    graph[row][col] = 1
    
    cnt = 1
    while queue:
        [crow, ccol] = queue.popleft()
        for i in range(4):
            nr, nc = crow + dr[i], ccol + dc[i]
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            if graph[nr][nc] == 1:
                continue
            graph[nr][nc] = 1
            queue.append([nr, nc])
            cnt += 1
    
    return cnt

def main():
    n, m, k = map(int, input().split())
    
    graph = [[0] * m for _ in range(n)]
    
    for _ in range(k):
        lc, lr, rc, rr = map(int, input().split())
        for row in range(lr, rr):
            for col in range(lc, rc):
                graph[row][col] = 1
    ans = []
    for row in range(n):
        for col in range(m):
            if graph[row][col] == 0:
                ans.append(bfs(row, col, graph, n, m))
    ans.sort()
    print(len(ans))
    print(*ans)
    
if __name__ == "__main__":
    main()