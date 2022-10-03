import sys

input = sys.stdin.readline

sudoku = [[] for _ in range(9)]
zeroPoint = []


def draw() -> None:
    for i in range(9):
        for j in range(9):
            print(sudoku[i][j], end=" ")
        print()


def isValid(col: int, row: int, val: int) -> bool:
    sc = col // 3 * 3
    sr = row // 3 * 3
    for i in range(3):
        for j in range(3):
            if (
                (sudoku[sc + i][sr + j] == val)
                or (sudoku[col][i * 3 + j] == val)
                or (sudoku[i * 3 + j][row] == val)
            ):
                return False
    return True


def solve(idx: int) -> None:
    if idx == len(zeroPoint):
        draw()
        exit(0)

    x = zeroPoint[idx][0]
    y = zeroPoint[idx][1]

    for v in range(1, 10):
        if isValid(y, x, v):
            sudoku[y][x] = v
            solve(idx + 1)

    sudoku[y][x] = 0


for i in range(9):
    sudoku[i] = list(map(int, input().split()))
    for j in range(9):
        if sudoku[i][j] == 0:
            zeroPoint.append([j, i])

solve(0)
