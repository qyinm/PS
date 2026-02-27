import heapq
import sys
input = sys.stdin.readline

DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def can_move(pos, next_pos, n, board, subsum_row, subsum_col):
    r, c = pos
    nr, nc = next_pos

    if nr < 0 or nr >= n or nc < 0 or nc >= n:
        return False
    if board[nr][nc] == '#' or board[nr][nc] == 'S':
        return False

    snake_in_way = True
    if nr == r:
        min_c, max_c = min(c, nc), max(c, nc)
        snake_in_way = (subsum_row[nr + 1][max_c + 1] - subsum_row[nr + 1][min_c]) == 0
    elif nc == c:
        min_r, max_r = min(r, nr), max(r, nr)
        snake_in_way = (subsum_col[nc + 1][max_r + 1] - subsum_col[nc + 1][min_r]) == 0
    return snake_in_way

def travel(n, board, start, target, subsum_row, subsum_col):
    qu = [(0, start, 1)]
    dist = [[[float('inf')] * n for _ in range(n)] for _ in range(6)]
    dist[1][start[0]][start[1]] = 0
    while qu:
        time, pos, jump = heapq.heappop(qu)
        if (pos[0], pos[1]) == target:
            return dist[jump][target[0]][target[1]]

        r, c = pos
        if dist[jump][r][c] != time:
            continue
        for dr, dc in DIRS:
            nr, nc = r + dr * jump, c + dc * jump
            if can_move((r, c), (nr, nc), n, board, subsum_row, subsum_col) and dist[jump][nr][nc] > time + 1:
                heapq.heappush(qu, (time + 1, (nr, nc), jump))
                dist[jump][nr][nc] = time + 1

            if jump < 5:
                nxt_jump = jump + 1
                nxt_time = time + (nxt_jump ** 2)
                if dist[nxt_jump][r][c] > nxt_time:
                    dist[nxt_jump][r][c] = nxt_time
                    heapq.heappush(qu, (nxt_time, pos, nxt_jump))

            for nxt_jump in range(jump - 1, 0, -1):
                nxt_time = time + 1
                if dist[nxt_jump][r][c] > nxt_time:
                    dist[nxt_jump][r][c] = nxt_time
                    heapq.heappush(qu, (nxt_time, pos, nxt_jump))
    return -1

def main():
    n = int(input())
    board = [list(input().rstrip()) for _ in range(n)]
    ans = []
    q = int(input())
    cache = dict({})
    subsum_row = [[0] * (n + 1) for _ in range(n + 1)]
    subsum_col = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(n):
        for j in range(n):
            subsum_row[i + 1][j + 1] = subsum_row[i + 1][j] + (1 if board[i][j] == '#' else 0)
            subsum_col[i + 1][j + 1] = subsum_col[i + 1][j] + (1 if board[j][i] == '#' else 0)

    for _ in range(q):
        s_r, s_c, t_r, t_c = map(int, input().split())
        start, target = (s_r - 1, s_c - 1), (t_r - 1, t_c - 1)
        if (start, target) not in cache.keys():
            cache[(start, target)] = travel(n, board, start, target, subsum_row, subsum_col)
        print(cache[(start, target)])

if __name__ == "__main__":
    main()
