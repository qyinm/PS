import sys
input = sys.stdin.readline

from collections import deque

DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(sr, sc, board, visited):
    qu = deque([(sr, sc)])

    treasure_group = [(sr, sc)]
    while qu:
        r, c = qu.popleft()

        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            
            if nr < 0 or nr >= 5 or nc < 0 or nc >= 5:
                continue
            if (nr, nc) in visited or board[nr][nc] != board[sr][sc]:
                continue
            visited.add((nr, nc))
            qu.append((nr, nc))
            treasure_group.append((nr, nc))

    return treasure_group

def find_treasure_value(board):
    visited = set()
    treasures = []
    treasure_value = 0
    for r in board:
        # print(*r)
        pass
    for r, row in enumerate(board):
        for c, value in enumerate(row):
            if (r, c) in visited and board[r][c] > 0:
                continue
            visited.add((r, c))
            treasure_group = bfs(r, c, board, visited)
            # print(treasure_group)
            if len(treasure_group) >= 3:
                treasures.append(treasure_group)
                treasure_value += len(treasure_group)
                # print(treasure_group)
    
    return (treasure_value, treasures)


def rotate(board, center):
    c_r, c_c = center
    tmp1, tmp2, tmp3 = board[c_r - 1][c_c + 1], board[c_r - 1][c_c], board[c_r - 1][c_c - 1]
    board[c_r - 1][c_c + 1] = board[c_r - 1][c_c - 1]
    board[c_r - 1][c_c] = board[c_r][c_c - 1]
    board[c_r - 1][c_c - 1] = board[c_r + 1][c_c - 1]
    board[c_r][c_c - 1] = board[c_r + 1][c_c]
    board[c_r + 1][c_c - 1] = board[c_r + 1][c_c + 1]
    board[c_r + 1][c_c] = board[c_r][c_c + 1]
    board[c_r + 1][c_c + 1] = tmp1
    board[c_r][c_c + 1] = tmp2

def main():
    k, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(5)]
    new_treasures = deque(list(map(int, input().split())))
    # 3. k번 반복 혹은 유물 더이상 획득 불가시
    for _ in range(k):
        answer = 0
        # 1. roation, one of 90, 180, 270
        # 유물 1차 획득 가치 > 회전 각도 최소 > 열 작은 순 > 행 작은 순
        CENTER_RANGE = [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
        rotate_results = []
        will_removes = [[0] * 9 for _ in range(3)]
        for center_idx, (c_r, c_c) in enumerate(CENTER_RANGE):
            rotate_board = [row[:] for row in board]
            for i in range(3):
                rotate(rotate_board, (c_r, c_c))
                value, will_remove = find_treasure_value(rotate_board)
                # print(will_remove)
                # print('-' * 30)
                rotate_results.append((-value, i, center_idx))
                will_removes[i][center_idx] = will_remove

        if len(rotate_results) == 0:
            break

        rotate_results.sort()
        rotate_value, rotate_state, center_idx = rotate_results[0]
        for _ in range(rotate_state + 1):
            rotate(board, CENTER_RANGE[center_idx])
        remove_groups = will_removes[rotate_state][center_idx]
        rotate_value = -rotate_value
        # print(rotate_results)
        # print(rotate_results)
        while rotate_value > 0:
            answer += rotate_value
            # 2. get treasure
            # 2-1 상하좌우 같은거 3개이상 연결된거 -> 사라짐. 가치 = 모인 조각 개수
            for remove_group in remove_groups:
                for (r, c) in remove_group:
                    board[r][c] = 0

            # 2-2
            # 벽면 M개 숫자 있는 거 사용
            # 순서대로 빈공간에 열 작은순 > 행 큰순 으로 배치된다.
            # 사용된거는 재사용 못하고 안사용한 것만 해야함
            # for r in board:
            #     print(*r)
            # print('-' * 30)
            refill_cells = []
            for c in range(5):
                for r in range(4, -1, -1):
                    if board[r][c] == 0:
                        refill_cells.append((r, c))
            min_len = min(len(new_treasures), len(refill_cells))
            for i in range(min_len):
                re_r, re_c = refill_cells[i]
                board[re_r][re_c] = new_treasures.popleft()
            
            # for r in board:
            #     print(*r)
            # print('-' * 30)
            # 2-3
            # 유물 연쇄 획득
            # 2-1로 다시 돌아가는거
            rotate_value, remove_groups = find_treasure_value(board)
        if answer == 0:
            break
        print(answer, end = ' ')

if __name__ == "__main__":
    main()