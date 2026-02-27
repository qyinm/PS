import sys
input = sys.stdin.readline
from collections import deque

DIRS = [(-1, 0), (0, -1), (0, 1), (1, 0)]
UP, LEFT, RIGHT, DOWN = 0, 1, 2, 3

def bfs(sr, sc, board, visited):
    n = len(board) - 1
    qu = deque([(sr, sc, 0)])
    local_visited = set()
    nomi = []
    while qu:
        qu_len = len(qu)
        for _ in range(qu_len):
            r, c, dist = qu.popleft()
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 < nr <= n and 0 < nc <= n and board[nr][nc] >= 0 and (nr, nc) not in visited and (nr, nc) not in local_visited:
                    qu.append((nr, nc, dist + 1))
                    local_visited.add((nr, nc))
                    if board[nr][nc] > 0:
                        nomi.append((dist + 1, nr, nc))
        if len(nomi) > 0:
            break
    nomi.sort()
    if len(nomi) == 0:
        return (sr, sc)
    # print(f'nomi: {nomi}')
    return (nomi[0][1], nomi[0][2])

def main():
    n, k, l = map(int, input().split())
    board = [[-1] * (n + 1) for _ in range(n + 1)]

    for r in range(1, n + 1):
        row = list(map(int, input().split()))
        for idx, val in enumerate(row):
            board[r][idx + 1] = val

    robots = [tuple(map(int, input().split())) for _ in range(k)]
    visited = set(robots)
    # show(board, visited)
    # print(visited)
    for _ in range(l):
        # move
        robot_count = len(robots)
        for idx, robot in enumerate(robots):
            r, c = robot
            if board[r][c] > 0:
                continue
            next_robot = bfs(r, c, board, visited)
            robots[idx] = next_robot
            visited.remove(robot)
            visited.add(next_robot)
        # show(board, visited)
        # clean
        for robot in robots:
            r, c = robot

            RANGE = [LEFT, UP, RIGHT, DOWN]
            clean_sum = []
            for prior, OUT_DIR in enumerate(RANGE):
                curr_sum = board[r][c]
                points = [(r, c)]
                for idx, (dr, dc) in enumerate(DIRS):
                    if idx == OUT_DIR:
                        continue
                    nr, nc = r + dr, c + dc

                    if not (0 < nr <= n and 0 < nc <= n) or board[nr][nc] == -1:
                        continue
                    curr_sum += min(20, board[nr][nc])
                    points.append((nr, nc))
                clean_sum.append((-curr_sum, prior, points))
            clean_sum.sort()
            clean_info = clean_sum[0]
            for (clean_r, clean_c) in clean_info[2]:
                board[clean_r][clean_c] = max(board[clean_r][clean_c] - 20, 0)
        # show(board, visited)
        # add dust & add expand dust list
        for r_idx, row in enumerate(board):
            for c_idx, val in enumerate(row):
                if val <= 0:
                    continue
                val += 5
                board[r_idx][c_idx] = val
        # show(board, visited)
        # expand dust
        added_dust = []
        for r_idx, row in enumerate(board):
            for c_idx, val in enumerate(row):
                if val != 0:
                    continue

                round_dust = 0
                for dr, dc in DIRS:
                    nr, nc = r_idx + dr, c_idx + dc
                    if nr <= 0 or nr > n or nc <= 0 or nc > n:
                        continue
                    if board[nr][nc] > 0:
                        round_dust += board[nr][nc]
                added_dust.append((round_dust // 10, (r_idx, c_idx)))
        for dust, (r, c) in added_dust:
            board[r][c] = dust
        # show(board, visited)

        # output
        print(sum(sum([max(r, 0) for r in row]) for row in board))
        # print('-' * 20)

if __name__ == "__main__":
    main()
