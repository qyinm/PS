import sys

input = sys.stdin.readline

def main():
    n, l = map(int, input().split())
    board: list[list[int]] = [list(map(int, input().split())) for _ in range(n)]

    ans = 0

    for i in range(n):
        flag = True
        j = 0
        prev_dir = None
        while j < n:
            tmp_idx = next((k for k in range(j + 1, n) if board[i][j] != board[i][k]), n)
            next_idx = next((k for k in range(tmp_idx + 1, n) if board[i][tmp_idx] != board[i][k]), n)
            if tmp_idx == n:
                break
            if abs(board[i][j] - board[i][tmp_idx]) > 1:
                flag = False
                break
            if board[i][j] < board[i][tmp_idx] and (j + l + l if prev_dir == "down" else j + l) <= tmp_idx:
                j = tmp_idx
                prev_dir = "up"
                continue
            if board[i][j] > board[i][tmp_idx] and tmp_idx + l <= next_idx:
                j = tmp_idx
                prev_dir = "down"
                continue
            flag = False
            break
        if flag:
            ans += 1
    for i in range(n):
        flag = True
        j = 0
        prev_dir = None
        while j < n:
            tmp_idx = next((k for k in range(j + 1, n) if board[j][i] != board[k][i]), n)
            next_idx = next((k for k in range(tmp_idx + 1, n) if board[tmp_idx][i] != board[k][i]), n)
            if tmp_idx == n:
                break
            if abs(board[j][i] - board[tmp_idx][i]) > 1:
                flag = False
                break
            if board[j][i] < board[tmp_idx][i] and (j + l + l if prev_dir == "down" else j + l) <= tmp_idx:
                j = tmp_idx
                prev_dir = "up"
                continue
            if board[j][i] > board[tmp_idx][i] and tmp_idx + l <= next_idx:
                j = tmp_idx
                prev_dir = "down"
                continue
            flag = False
            break
        if flag:
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()