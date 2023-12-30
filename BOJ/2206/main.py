from collections import deque

INF = float('inf')

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs():
    n, m = map(int, input().split())
    graph = []
    for _ in range(n):
        graph.append([*map(int, input())])
    cache = [[[-1] * m for _ in range(n)] for _ in range(2)]
    queue = deque([])
    queue.append([0, 0, 1])
    cache[1][0][0] = 1
    while queue:
        cur = queue.popleft()
        if cur[0] == n-1 and cur[1] == m-1:
            return cache[cur[2]][n-1][m-1]
        for i in range(4):
            nr, nc = cur[0]+dr[i], cur[1]+dc[i]
            count = cur[2]
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            if cache[count][nr][nc] != -1:
                continue
            if count == 0 and graph[nr][nc] == 1:
                continue
            if graph[nr][nc] == 1:
                count -= 1
            cache[count][nr][nc] = cache[cur[2]][cur[0]][cur[1]] + 1
            queue.append([nr, nc, count])
            
    return -1
def main():
    answer = bfs()
    print(answer)

if __name__ == "__main__":
    main()
