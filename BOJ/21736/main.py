from collections import deque

def getStart(N, M, board):
    for y in range(N):
        for x in range(M):
            if board[y][x] == 'I':
                return y, x

def main():
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]
    sy, sx = getStart(N, M, board)

    q = deque([(sy, sx)])
    cnt = 0
    visited = [[False] * M for _ in range(N)]
    visited[sy][sx] = True
    weight = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while q:
        cy, cx = q.popleft()
        
        if board[cy][cx] == 'P':
            cnt += 1
        
        for wy, wx in weight:
            ny, nx = cy + wy, cx + wx
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            if visited[ny][nx] or board[ny][nx] == 'X':
                continue
            visited[ny][nx] = True
            q.append((ny, nx))
    
    print(cnt if cnt > 0 else 'TT')   

if __name__ == "__main__":
    main()