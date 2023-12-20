from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

def get_start(graph, w, h, queue, fireq):
    for r in range(h):
        for c in range(w):
            if graph[r][c] == '@':
                queue.append([r, c])
            elif graph[r][c] == '*':
                fireq.append([r, c])
    
def valid_next(graph, nr, nc, h, w):
    
    if nr < 0 or nr >= h or nc < 0 or nc >= w:
        return False
    return True
    
def end_point(r, c, h, w):
    return r == 0 or r == h-1 or c == 0 or c == w-1

def bfs(graph, w, h):
    queue = deque([])
    fireq = deque([])
    
    get_start(graph, w, h, queue, fireq)
    
    visited = [[-1] * w for _ in range(h)]
    visited[queue[0][0]][queue[0][1]] = 1
    
    while queue:
        newqueue = deque([])
        newfireq = deque([])
        while queue:
            cr, cc = queue.popleft()
            if graph[cr][cc] == '*':
                continue
            if end_point(cr, cc, h, w):
                return visited[cr][cc]
            for i in range(4):
                nr, nc = cr + dr[i], cc + dc[i]
                if not valid_next(graph, nr, nc, h, w):
                    continue
                if graph[nr][nc] == '*' or graph[nr][nc] == '#':
                    continue
                if visited[nr][nc] != -1:
                    continue
                
                visited[nr][nc] = visited[cr][cc] + 1
                newqueue.append([nr, nc])
        while newqueue:
            queue.append(newqueue.popleft())
        while fireq:
            fcr, fcc = fireq.popleft()
            for i in range(4):
                fnr, fnc = fcr + dr[i], fcc + dc[i]
                if not valid_next(graph, fnr, fnc, h, w):
                    continue
                if graph[fnr][fnc] == '*' or graph[fnr][fnc] == '#':
                    continue
                graph[fnr][fnc] = '*'
                newfireq.append([fnr, fnc])
        while newfireq:
            fireq.append(newfireq.popleft())
    return -1
    

def main():
    tc = int(input())
    ans = []
    for _ in range(tc):
        w, h = map(int, input().split())
        graph = [[*input().rstrip()] for _ in range(h)]
        ans.append(bfs(graph, w, h))
    for a in ans:
        if a == -1:
            print("IMPOSSIBLE")
        else:
            print(a)
    
if __name__ == "__main__":
    main()
