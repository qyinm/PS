from collections import deque
import sys
input = sys.stdin.readline

row, col = 0, 0
graph = []
visited = []
dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]

MOUNT = '#'
GRASS = '.'
ICE = '+'
WOLF = 'W'

def is_valid(r, c):
    return 0 <= r and r < row and 0 <= c and c < col and graph[r][c] != MOUNT

def bfs(r, c):
    
    queue = deque([])
    
    for d in range(4):
        visited[r][c][d] = True
        queue.append((r, c, d))
    
    while queue:
        (cr, cc, direction) = queue.popleft()
        nr, nc = cr+dr[direction], cc+dc[direction]
        if graph[cr][cc] == ICE and graph[nr][nc] != '#':
            if not is_valid(nr, nc):
                continue
            if visited[nr][nc][direction]:
                continue
            visited[nr][nc][direction] = True
            queue.append((nr, nc, direction))
        else:
            for i in range(4):
                nr, nc = cr+dr[i], cc+dc[i]
                if not is_valid(nr, nc):
                    continue
                if visited[nr][nc][i]:
                    continue
                visited[nr][nc][i] = True
                queue.append((nr, nc, i))
                
                
def logic():
    for r in range(row):
        for c in range(col):
            if graph[r][c] != WOLF:
                continue
            bfs(r, c)
    
    for r in range(row):
        for c in range(col):
            if graph[r][c] != GRASS:
                continue
            if all(v == False for v in visited[r][c]):
                graph[r][c] = 'P'
    
    
    for g in graph:
        print(''.join(g))

def main():
    global row, col, graph, visited
    row, col = map(int, input().split())
    graph = [[*input().rstrip()] for _ in range(row)]
    visited = [[[False] * 4 for _ in range(col)] for _ in range(row)]
    logic()
    pass
    
if __name__ == "__main__":
    main()