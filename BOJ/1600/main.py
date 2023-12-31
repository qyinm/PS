from collections import deque
horse_dr = [-2, -1, 1, 2, -2, 2, -1, 1]
horse_dc = [1, 2, 2, 1, -1, -1, -2, -2]
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def valid(crow, ccol, row, col):
    return 0 <= crow and crow < row and 0 <= ccol and ccol < col

def bfs(graph, r, c, k):
    cache = [[[-1] * c for _ in range(r)] for _ in range(k+1)]
    
    queue = deque([])
    cache[k][0][0] = 0
    queue.append([0, 0, k])
    while queue:
        crow, ccol, ccnt = queue.popleft()
        if crow == r-1 and ccol == c-1:
            return cache[ccnt][crow][ccol]
        if ccnt > 0:
            for h in range(len(horse_dr)):
                nr, nc = crow + horse_dr[h], ccol + horse_dc[h]
                if not valid(nr, nc, r, c) or graph[nr][nc] == 1:
                    continue
                if cache[ccnt-1][nr][nc] != -1:
                    continue
                cache[ccnt-1][nr][nc] = cache[ccnt][crow][ccol] + 1
                queue.append([nr, nc, ccnt - 1])
        for d in range(len(dr)):
            nr, nc = crow + dr[d], ccol + dc[d]
            if not valid(nr, nc, r, c) or graph[nr][nc] == 1:
                continue
            if cache[ccnt][nr][nc] != -1:
                continue
            cache[ccnt][nr][nc] = cache[ccnt][crow][ccol] + 1
            queue.append([nr, nc, ccnt])
    
    return -1
    

def main():
    k = int(input())
    c, r = map(int, input().split())
    graph = [[*map(int, input().split())] for _ in range(r)]
    
    answer = bfs(graph, r, c, k)
    print(answer)

if __name__ == "__main__":
    main()
