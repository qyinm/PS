from collections import deque

directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def isMoreNear(direction, pointR, pointB):
    if direction == 0:
        return 'R' if pointR[1] < pointB[1] else 'B'
    elif direction == 1:
        return 'R' if pointR[1] > pointB[1] else 'B'
    elif direction == 2:
        return 'R' if pointR[0] < pointB[0] else 'B'
    elif direction == 3:
        return 'R' if pointR[0] > pointB[0] else 'B'
    
    return None

def getNextPoint(direction, pointR, pointB, board):
    color = isMoreNear(direction, pointR, pointB)

    points = [pointR, pointB]
    flag = 0
    if color == 'R':
        while True:
            y, x = pointR
            ny, nx = y + directions[direction][0], x + directions[direction][1]
            if board[ny][nx] == '#':
                break
            if board[ny][nx] == 'O':
                flag = 2
                pointR = (-1, -1)
                break
            pointR = (ny, nx)
        while True:
            y, x = pointB
            ny, nx = y + directions[direction][0], x + directions[direction][1]
            if board[ny][nx] == '#' or (ny, nx) == pointR:
                break
            if board[ny][nx] == 'O':
                return (1, (), ())
            pointB = (ny, nx)

    elif color == 'B':
        while True:
            y, x = pointB
            ny, nx = y + directions[direction][0], x + directions[direction][1]
            if board[ny][nx] == '#':
                break
            if board[ny][nx] == 'O':
                return (1, (), ())
            pointB = (ny, nx)
        while True:
            y, x = pointR
            ny, nx = y + directions[direction][0], x + directions[direction][1]
            if board[ny][nx] == '#' or (ny, nx) == pointB:
                break
            if board[ny][nx] == 'O':
                flag = 2
                break
            pointR = (ny, nx)
    return (flag, pointR, pointB)


def bfs(pointR, pointB, board, N, M):
    q = deque()
    q.append(pointR)
    q.append(pointB)
    visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
    visited[pointR[0]][pointR[1]][pointB[0]][pointB[1]] = True

    cnt = 1
    while len(q) > 0 and cnt <= 10:
        for i in range(len(q)//2):
            currPr = q.popleft()
            currPb = q.popleft()

            for i in range(4):
                flag, nPr, nPb = getNextPoint(i, currPr, currPb, board)
                if flag == 2:
                    return cnt
                if flag == 1:
                    continue
                # print(flag, nPr, nPb)
                if visited[nPr[0]][nPr[1]][nPb[0]][nPb[1]]:
                    continue
                visited[nPr[0]][nPr[1]][nPb[0]][nPb[1]] = True
                q.append(nPr)
                q.append(nPb)
        cnt += 1
    return -1

def main():
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]
    
    for y in range(N):
        for x in range(M):
            if board[y][x] == 'R':
                pointR = (y, x)
                board[y][x] = '.'
            elif board[y][x] == 'B':
                pointB = (y, x)
                board[y][x] = '.'
    # print(pointR, pointB)
    print(bfs(pointR, pointB, board, N, M))

if __name__ == "__main__":
    main()