from collections import deque

weights = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(visited, board, R, C, r, c):
    qu = deque()
    qu.append((r, c))
    visited[r][c] = True
    wolf_cnt = 0
    sheep_cnt = 0

    while len(qu) > 0:
        cr, cc = qu.popleft()
        if board[cr][cc] == 'v':    wolf_cnt += 1
        elif board[cr][cc] == 'k':  sheep_cnt += 1

        for (wr, wc) in weights:
            nr, nc = cr + wr, cc + wc
            if nr < 0 or nr >= R or nc < 0 or nc >= C:  continue
            if visited[nr][nc] or board[nr][nc] == '#':    continue
            qu.appendleft((nr, nc))
            visited[nr][nc] = True
    # print(f"r: {r}, c: {c}, s: {sheep_cnt}, w: {wolf_cnt}")
    if sheep_cnt > wolf_cnt:
        return (wolf_cnt, 0)
    return (0, sheep_cnt)

def main():
    R, C = map(int, input().split())
    board = []

    wolf, sheep = 0, 0
    for _ in range(R):
        board.append(list(input()))
    for row in board:
        for el in row:
            if el == 'v':   wolf += 1
            elif el == 'k': sheep += 1
    
    visited = [[False for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if board[r][c] == '#':  continue
            if visited[r][c]:   continue
            ret = bfs(visited, board, R, C, r, c)
            wolf -= ret[0]
            sheep -= ret[1]
    
    print(sheep, wolf)
    
if __name__ == "__main__":
    main()