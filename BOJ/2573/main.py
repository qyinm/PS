from collections import deque
import sys

input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
r, c = 0, 0

def valid(row, col):
    return 0 <= row and row < r and 0 <= col and col < c

def check_ice(row, col, ice_berge):
    cnt = 0
    for i in range(4):
        nr, nc = row+dr[i], col+dc[i]
        if not valid(nr, nc):
            continue
        if ice_berge[nr][nc] == 0:
            cnt += 1
    return (ice_berge[row][col] <= cnt, cnt)

def init(iceq, ice_berge):
    for row, ices in enumerate(ice_berge):
        for col, ice in enumerate(ices):
            if ice != 0:
                iceq.append((row, col))
                return

def main():
    global r, c
    r, c = map(int, input().split())
    ice_berge = [[*map(int, input().split())] for _ in range(r)]
    iceq = deque([])
    init(iceq, ice_berge)
    
    ans = 0
    while len(iceq) == 1:
        temp_ice = deque([])
        visited = [[False] * c for _ in range(r)]
        visited[iceq[0][0]][iceq[0][1]] = True
        temp_ice.append(iceq[0])
        while iceq:
            (row, col) = iceq.popleft()
            for i in range(4):
                nr, nc = row+dr[i], col+dc[i]
                if not valid(nr, nc) or ice_berge[nr][nc] == 0:
                    continue
                if visited[nr][nc]:
                    continue
                temp_ice.append((nr, nc))
                iceq.append((nr, nc))
                visited[nr][nc] = True
        #print(f'temp_ice {temp_ice}')        
        zeroq = deque([])
        ice_group = deque([])
        while temp_ice:
            (trow, tcol) = temp_ice.popleft()
            (is_zero, melt) = check_ice(trow, tcol, ice_berge)
            if is_zero:
                zeroq.append((trow, tcol))
            else:
                ice_berge[trow][tcol] -= melt
                ice_group.append((trow, tcol))
        #print(f'zeroq {zeroq}')
        #print(f'ice_group {ice_group}')
        while zeroq:
            (zr, zc) = zeroq.popleft()
            ice_berge[zr][zc] = 0
        group_visited = [[False] * c for _ in range(r)]
        if not ice_group:
            print(0)
            exit(0)
        while ice_group:
            (row, col) = ice_group.popleft()
            if group_visited[row][col]:
                continue
            group_visited[row][col] = True
            iceq.append((row,col))
            groupq = deque([(row, col)])
            while groupq:
                (cr, cc) = groupq.popleft()
                for i in range(4):
                    nr, nc = cr+dr[i], cc+dc[i]
                    if not valid(nr, nc) or ice_berge[nr][nc] == 0:
                        continue
                    if group_visited[nr][nc]:
                        continue
                    groupq.append((nr, nc))
                    group_visited[nr][nc] = True
        ans += 1
    print(ans)
if __name__ == "__main__":
    main()
