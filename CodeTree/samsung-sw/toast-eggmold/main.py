from collections import deque

DIRS = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def bfs(start_pos, visited, egg_board, l, r):
    n = len(egg_board)

    qu = deque([start_pos])
    egg_group = [start_pos]
    while qu:
        egg_r, egg_c = qu.popleft()
        
        for dr, dc in DIRS:
            egg_nr, egg_nc = egg_r + dr, egg_c + dc

            if egg_nr < 0 or egg_nr >= n or egg_nc < 0 or egg_nc >= n:
                continue
            if (egg_nr, egg_nc) in visited:
                continue
            if l <= abs(egg_board[egg_r][egg_c] - egg_board[egg_nr][egg_nc]) <= r:
                next_point = (egg_nr, egg_nc)
                visited.add(next_point)
                qu.append(next_point)
                egg_group.append(next_point)
    
    return egg_group


def main():
    n, l, r = map(int, input().split())

    egg_board = [list(map(int, input().split())) for _ in range(n)]
    # print(egg_board)
    ans = 0
    while True:
        egg_groups = []
        visited = set()
        for row_index, row in enumerate(egg_board):
            for col_index, egg in enumerate(row):
                if (row_index, col_index) in visited:
                    continue
                visited.add((row_index, col_index))
                egg_group = bfs((row_index, col_index), visited, egg_board, l, r)
                if len(egg_group) == 1:
                    continue
                egg_groups.append(egg_group)
        if len(egg_groups) == 0:
            break
        for egg_group in egg_groups:
            val = sum(egg_board[egg_r][egg_c] for egg_r, egg_c in egg_group) // len(egg_group)
            for egg_r, egg_c in egg_group:
                egg_board[egg_r][egg_c] = val
        ans += 1

    print(ans)

if __name__ == "__main__":
    main()