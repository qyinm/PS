from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def show(graph):
    for gr in graph:
        for g in gr:
            print(g, end = " ")
        print("")

def valid_point(row, col, n, m):
    return 0 <= row and row < n and 0 <= col and col < m

def valid_cheese(row, col, graph, n, m, visited):
    wall = 0
    for i in range(4):
        nr, nc = row + dr[i], col + dc[i]
        if not valid_point(nr, nc, n, m):
            continue
        if graph[nr][nc] == 0 and visited[nr][nc]:
            wall += 1
    return wall >= 2

def bfs(row, col, graph, visited, n, m, delq):
    q = deque([(row, col)])
    visited[row][col] = True
    cheese_cnt = 0

    while q:
        cr, cc = q.popleft()
        
        for i in range(4):
            nr, nc = cr + dr[i], cc + dc[i]
            if not valid_point(nr, nc, n, m) or visited[nr][nc]:
                continue
            visited[nr][nc] = True
            if graph[nr][nc] == 1:
                cheese_cnt += 1
                delq.append((nr, nc))
            else:
                q.append((nr, nc))
    return cheese_cnt

    
def main():
    n, m = map(int, input().split())
    graph = [[*map(int, input().split())] for _ in range(n)]
    
    ans = 0
    while True:
        visited = [[False] * m for _ in range(n)]
        delq = deque([])
        cnt = 0
        for i in range(n):
            for j in range(m):
                if (i == 0 or i == n-1) or (j == 0 or j == m-1) and not visited[i][j]:
                    cnt += bfs(i, j, graph, visited, n, m, delq)
        
        zeroq = deque([])
        while delq:
            delr, delc = delq.popleft()
            if valid_cheese(delr, delc, graph, n, m, visited):
                zeroq.append((delr, delc))
        while zeroq:
            r, c = zeroq.popleft()
            graph[r][c] = 0
        '''
        print("--------------------------------")
        show(graph)
        print("--------------------------------")
        '''
        if cnt == 0:
            break
        ans += 1
    print(ans)

if __name__ == "__main__":
    main()
