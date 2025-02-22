from collections import deque
import sys
input = sys.stdin.readline

def move(n, board, direction):
    new_board = [row[:] for row in board]
    if direction == 0:
        for col in range(n):
            pos = 0
            for row in range(1, n):
                if new_board[row][col] == 0:
                    continue
                temp = new_board[row][col]
                new_board[row][col] = 0
                if new_board[pos][col] == 0:
                    new_board[pos][col] = temp
                elif new_board[pos][col] == temp:
                    new_board[pos][col] *= 2
                    pos += 1
                else:
                    pos += 1
                    new_board[pos][col] = temp
    elif direction == 1:
        for col in range(n):
            pos = n - 1
            for row in range(n - 2, -1, -1):
                if new_board[row][col] == 0:
                    continue
                temp = new_board[row][col]
                new_board[row][col] = 0
                if new_board[pos][col] == 0:
                    new_board[pos][col] = temp
                elif new_board[pos][col] == temp:
                    new_board[pos][col] *= 2
                    pos -= 1
                else:
                    pos -= 1
                    new_board[pos][col] = temp
    elif direction == 2:
        for row in range(n):
            pos = 0
            for col in range(1, n):
                if new_board[row][col] == 0:
                    continue
                temp = new_board[row][col]
                new_board[row][col] = 0
                if new_board[row][pos] == 0:
                    new_board[row][pos] = temp
                elif new_board[row][pos] == temp:
                    new_board[row][pos] *= 2
                    pos += 1
                else:
                    pos += 1
                    new_board[row][pos] = temp
    else:
        for row in range(n):
            pos = n - 1
            for col in range(n - 2, -1, -1):
                if new_board[row][col] == 0:
                    continue
                temp = new_board[row][col]
                new_board[row][col] = 0
                if new_board[row][pos] == 0:
                    new_board[row][pos] = temp
                elif new_board[row][pos] == temp:
                    new_board[row][pos] *= 2
                    pos -= 1
                else:
                    pos -= 1
                    new_board[row][pos] = temp
    return new_board

def find_max(board):
    return max(map(max, board))

def bfs(n, board):
    queue = deque()
    queue.append(board)
    ans = find_max(board)
    for _ in range(5):
        next_queue = deque()
        visited_set = set()
        while queue:
            curr = queue.popleft()
            curr_max = find_max(curr)
            ans = max(ans, curr_max)
            for direction in range(4):
                new_brd = move(n, curr, direction)
                if new_brd != curr:
                    brd_tuple = tuple(tuple(row) for row in new_brd)
                    if brd_tuple in visited_set:
                        continue
                    visited_set.add(brd_tuple)
                    next_queue.append(new_brd)
        queue = next_queue
    while queue:
        curr = queue.popleft()
        ans = max(ans, find_max(curr))
    return ans

def main():
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    print(bfs(n, board))

if __name__ == "__main__":
    main()