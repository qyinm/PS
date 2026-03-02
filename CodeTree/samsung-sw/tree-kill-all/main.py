DIRS = [(0, -1), (0, 1), (1,0), (-1, 0)]
XDIRS = [(1, -1), (1, 1), (-1, -1), (-1, 1)]

def main():
    n, m, k, cc = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    hearb = [[0] * n for _ in range(n)]

    ans = 0

    for _ in range(m):
        for r in range(n):
            for c in range(n):
                hearb[r][c] = max(hearb[r][c] - 1, 0)

        trees = [(r, c) for r in range(n) for c in range(n) if board[r][c] > 0]
        # 성장
        for r, c in trees:
            cnt = 0
            for dr, dc in DIRS:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < n and 0 <= nc < n and board[nr][nc] > 0:
                    cnt += 1
            board[r][c] += cnt
        
        # 3. 번식
        new_trees = []
        for r, c in trees:
            tmp = []
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == 0 and hearb[nr][nc] == 0:
                    tmp.append((nr, nc))
            if len(tmp) == 0:
                continue
            val = board[r][c] // len(tmp)
            new_trees.append((val, tmp))

        for val, poss in new_trees:
            for r, c in poss:
                board[r][c] += val

        trees = [(r, c) for r in range(n) for c in range(n) if board[r][c] > 0]

        # 제초!
        maxx = []
        for r, c in trees:
            curr_sum = board[r][c]
            remove_list = [(r, c)]
            for dr, dc in XDIRS:
                nr, nc = r, c
                for _ in range(k):
                    nr += dr
                    nc += dc
                    if not (0 <= nr < n and 0 <= nc < n) or board[nr][nc] == -1:
                        break
                    remove_list.append((nr, nc))
                    if board[nr][nc] <= 0:
                        break
                    curr_sum += board[nr][nc]
            maxx.append((-curr_sum, r, c, remove_list))

        if len(maxx) == 0:
            break

        maxx.sort()
        maxx_remove = maxx[0][3]
        for r, c in maxx_remove:
            board[r][c] = 0
            hearb[r][c] = cc + 1

        ans += -maxx[0][0]

    print(ans)

if __name__ == "__main__":
    main()