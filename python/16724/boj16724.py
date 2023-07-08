DIR = {"D": (0, 1),
        "U": (0, -1),
        "L": (-1, 0),
        "R": (1, 0),}

ans = 0
n, m = map(int,input().split())

check = [[0] * m for _ in range(n)]
board = []
for _ in range(n):
    board.append(list(input()))


def dfs(x: int, y: int, flag: int) -> int:
    wx, wy = DIR[board[y][x]]
    nx, ny = x+wx, y+wy
    
    if check[ny][nx] != 0:
        if check[ny][nx] == flag:
            return 1
        else:
            return 0
    
    check[ny][nx] = flag
    return dfs(nx, ny, flag)

ans = 0
flag = 1
for i in range(n):
    for j in range(m):
        if check[i][j] != 0:    continue
        check[i][j] = flag
        ans += dfs(j, i, flag)
        flag += 1
print(ans)