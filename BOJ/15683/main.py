import sys

input = sys.stdin.readline

# (up, down, left, right)
DIR = {
    1: [(0, 0, 0, 1), (0, 0, -1, 0), (0, 1, 0, 0), (-1, 0, 0, 0)],
    2: [(0, 0, -1, 1), (-1, 1, 0, 0)],
    3: [(-1, 0, 0, 1), (0, 1, 0, 1), (0, 1, -1, 0), (-1, 0, -1, 0)],
    4: [(-1, 0, -1, 1), (-1, 1, 0, 1), (0, 1, -1, 1), (-1, 1, -1, 0)],
    5: [(-1, 1, -1, 1)]
}

def count_blind_spots(board):
    return sum(row.count(0) for row in board)

def dfs(n, m, board, cctvs, cctvs_idx):
    if cctvs_idx == len(cctvs):
        return count_blind_spots(board)
    
    y, x = cctvs[cctvs_idx]
    answer = float('inf')
    for dir in DIR[board[y][x]]:
        up, down, left, right = dir
        prev_board = [row[:] for row in board]
        cur_up, cur_down, cur_left, cur_right = y, y, x, x
        
        while up != 0 and cur_up > 0:
            if board[cur_up][x] == 6:
                break

            cur_up += up
            if board[cur_up][x] == 0:
                board[cur_up][x] = '#'
            

        while down != 0 and cur_down < n - 1:
            if board[cur_down][x] == 6:
                break

            cur_down += down
            if board[cur_down][x] == 0:
                board[cur_down][x] = '#'

        while left != 0 and cur_left > 0:
            if board[y][cur_left] == 6:
                break

            cur_left += left
            if board[y][cur_left] == 0:
                board[y][cur_left] = '#'
        
        while right != 0 and cur_right < m - 1:
            if board[y][cur_right] == 6:
                break

            cur_right += right
            if board[y][cur_right] == 0:
                board[y][cur_right] = '#'

        answer = min(answer, dfs(n, m, board, cctvs, cctvs_idx + 1))

        board = prev_board

    return answer

def main():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    cctvs = []
    for i in range(n):
        for j in range(m):
            if board[i][j] < 6 and board[i][j] > 0:
                cctvs.append((i, j))

    print(dfs(n, m, board, cctvs, 0))

if __name__ == "__main__":
    main()