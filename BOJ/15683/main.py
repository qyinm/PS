import sys

input = sys.stdin.readline

UP, DOWN, LEFT, RIGHT = (-1, 0), (1, 0), (0, -1), (0, 1)

CCTV_DIRS = {
    1: [[RIGHT], [LEFT], [DOWN], [UP]],
    2: [[LEFT, RIGHT], [UP, DOWN]],
    3: [[UP, RIGHT], [DOWN, RIGHT], [DOWN, LEFT], [UP, LEFT]],
    4: [[UP, LEFT, RIGHT], [UP, DOWN, RIGHT], [DOWN, LEFT, RIGHT], [UP, DOWN, LEFT]],
    5: [[UP, DOWN, LEFT, RIGHT]],
}

def fill(board, y, x, dy, dx, n, m):
    filled = []
    ny, nx = y + dy, x + dx
    while 0 <= ny < n and 0 <= nx < m and board[ny][nx] != 6:
        if board[ny][nx] == 0:
            board[ny][nx] = '#'
            filled.append((ny, nx))
        ny += dy
        nx += dx
    return filled

def dfs(n, m, board, cctvs, idx):
    if idx == len(cctvs):
        return sum(row.count(0) for row in board)

    y, x = cctvs[idx]
    result = float('inf')

    for dirs in CCTV_DIRS[board[y][x]]:
        filled = []
        for dy, dx in dirs:
            filled += fill(board, y, x, dy, dx, n, m)

        result = min(result, dfs(n, m, board, cctvs, idx + 1))

        for fy, fx in filled:
            board[fy][fx] = 0

    return result

def main():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    cctvs = [(i, j) for i in range(n) for j in range(m) if 0 < board[i][j] < 6]

    print(dfs(n, m, board, cctvs, 0))

if __name__ == "__main__":
    main()
