import sys
from collections import deque

input = sys.stdin.readline

weights = [(1, 0), (-1, 0), (0, 1), (0, -1)]

N, M, P = map(int, input().split())
SP = list(map(int, input().split()))
board = [list(input()) for _ in range(N)]

castles = [[] for _ in range(P)]
castleSizes = [0] * P
for i in range(N):
    for j in range(M):
        if board[i][j].isdigit():
            castles[int(board[i][j]) - 1].append((0, i, j))
            castleSizes[int(board[i][j]) - 1] += 1
            
while True:
    flag = True
    newCastles = [[] for _ in range(P)]
    for who, castle in enumerate(castles):
        tq = deque()
        for ca in castle:
            tq.append(tuple(ca))

        while len(tq) > 0:
            (c, ty, tx) = tq.popleft()
            if c == SP[who]:
                newCastles[who].append((0, ty, tx))
                continue
            for (wy, wx) in weights:
                ny, nx = ty + wy, tx + wx
                if ny < 0 or ny >= N or nx < 0 or nx >= M:
                    continue
                if board[ny][nx] != '.':
                    continue
                board[ny][nx] = str(who + 1)
                tq.append((c+1, ny, nx))
                castleSizes[who] += 1
                flag = False
    for i in range(P):
        castles[i] = newCastles[i]
    if flag:
        break
    # for b in board:
    #     print(b)
    # print()
print(*castleSizes)