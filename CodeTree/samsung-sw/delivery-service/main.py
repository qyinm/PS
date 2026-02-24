import sys
from typing import NamedTuple

input = sys.stdin.readline

class Box(NamedTuple):
    number: int
    height: int
    width: int
    left: int

def gravity(board, box_map):
    visited = set()
    n = len(board)
    
    for row in range(n - 2, -1, -1):
        for col in range(n):
            if board[row][col] is None:
                continue
            if board[row][col] in visited:
                continue
            visited.add(board[row][col])
            box = box_map[board[row][col]]
            
            left = col
            right = col + box.width - 1

            can_down_row = row
            while can_down_row < n - 1 and can_down(can_down_row, left, right, board):
                can_down_row += 1
            
            if can_down_row == row:
                continue

            box_number = board[row][col]
            
            for remove_row in range(row, row - box.height, -1):
                for remove_col in range(left, right + 1):
                    board[remove_row][remove_col] = None  

            for add_row in range(can_down_row, can_down_row - box.height, -1):
                for add_col in range(left, right + 1):
                    board[add_row][add_col] = box_number

def is_can_remove(board, left, right, up, down, is_left) -> bool:
    n = len(board)
    if is_left:
        return all(board[row][col] is None for row in range(up, down) for col in range(0, left))
    else:
        return all(board[row][col] is None for row in range(up, down) for col in range(right + 1, n))

def can_down(height, left, right, board) -> bool:
    return all(board[height + 1][idx] is None for idx in range(left, right + 1))

def remove_box(board, box_map, is_left):
    n = len(board)
    visited = set()
    detected = []
    for row in range(n):
        for col in range(n - 1, -1, -1):
            if board[row][col] is None:
                continue
            if board[row][col] in visited:
                continue
            visited.add(board[row][col])
            box = box_map[board[row][col]]
            if not is_can_remove(board, box.left, box.left + box.width - 1, row, row + box.height, is_left):
                continue
            detected.append((board[row][col], row))
            break
    
    # remove detected box
    detected.sort()

    remove_box = detected[0]
    s_h = remove_box[1]
    box = box_map[remove_box[0]]

    for r in range(s_h, s_h + box.height):
        for c in range(box.left, box.left + box.width):
            board[r][c] = None    
    gravity(board, box_map)

    return remove_box[0]

def main():
    n, m = map(int, input().split())
    
    board = [[None] * n for _ in range(n)]
    boxes = []
    box_map = {}
    answer = []

    for _ in range(m):
        k, h, w, c = map(int, input().split())
        box = Box(k, h, w, c - 1)
        boxes.append(box)
        box_map[k] = box

    # stacking box
    for box in boxes:

        cur_h = box.height - 1
        cur_l = box.left
        cur_r = box.left + box.width - 1

        while cur_h < n - 1 and can_down(cur_h, cur_l, cur_r, board):
            cur_h += 1

        for r in range(cur_h - box.height + 1, cur_h + 1):
            for c in range(cur_l, cur_r + 1):
                board[r][c] = box.number

    # out box
    is_left = True
    while any(board[row][col] != None for row in range(n) for col in range(n)):
        answer.append(remove_box(board, box_map, is_left))
        is_left = not is_left

    print(*answer, sep = '\n')

if __name__ == "__main__":
    main()