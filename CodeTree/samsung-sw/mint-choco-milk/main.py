import sys
input = sys.stdin.readline
from collections import deque

MINT = frozenset({'T'})
CHOCO = frozenset({'C'})
MILK = frozenset({'M'})

CHOCO_MILK = CHOCO | MILK
MINT_MILK = MINT | MILK
MINT_CHOCO = MINT | CHOCO
MINT_CHOCO_MILK = MINT | CHOCO | MILK

FLAVOR, TRUST = range(2)

keys = [MINT_CHOCO_MILK, MINT_CHOCO, MINT_MILK, CHOCO_MILK, MILK, CHOCO, MINT]

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

def mix(attack, base, status):
    if status == "strong":
        return attack
    return attack | base

def is_valid_range(r, c, n):
    return 0 <= r < n and 0 <= c < n

def bfs(r, c, board, visited) -> (int, int):
    members = [(-board[r][c][TRUST], r, c)]
    queue = deque([(r, c)])
    visited[r][c] = True
    n = len(board)

    while queue:
        cu_r, cu_c = queue.popleft()

        for rw, cw in zip(dr, dc):
            ne_r, ne_c = cu_r + rw, cu_c + cw

            if not is_valid_range(ne_r, ne_c, n):
                continue
            if board[ne_r][ne_c][0] != board[r][c][0] or visited[ne_r][ne_c]:
                continue
            visited[ne_r][ne_c] = True
            queue.append((ne_r, ne_c))
            members.append((-board[ne_r][ne_c][1], ne_r, ne_c))

    members.sort()
    for member in members[1:]:
        _, m_r, m_c = member
        board[m_r][m_c][TRUST] -= 1
    leader = members[0]
    board[leader[1]][leader[2]][TRUST] += len(members) - 1
    return (
        len(board[leader[1]][leader[2]][FLAVOR]),
        -board[leader[1]][leader[2]][TRUST],
        members[0][1],
        members[0][2]
    )

def main():
    n, t = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(n)]
    trusts = [list(map(int, input().rstrip().split())) for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            board[i][j] = [frozenset({board[i][j]}), trusts[i][j], None]

    for _ in range(t):
        # morning
        for row in board:
            for col in row:
                col[1] += 1

        # launch
        leaders = []
        visited = [[False] * n for _ in range(n)]

        for r in range(n):
            for c in range(n):
                if visited[r][c]:
                    continue
                leader = bfs(r, c, board, visited)
                leaders.append(leader)
        
        leaders.sort()

        # dinner
        attacked = set()
        for leader in leaders:
            _, _, leader_r, leader_c = leader
            if (leader_r, leader_c) in attacked:
                continue
            trust_power = board[leader_r][leader_c][TRUST]
            attack_power = trust_power - 1
            dir = trust_power % 4
            board[leader_r][leader_c][TRUST] = 1
            next_r, next_c = leader_r + dr[dir], leader_c + dc[dir]

            while is_valid_range(next_r, next_c, n) and attack_power > 0:
                if board[next_r][next_c][FLAVOR] == board[leader_r][leader_c][FLAVOR]:
                    next_r, next_c = next_r + dr[dir], next_c + dc[dir]
                    continue
                if attack_power > board[next_r][next_c][TRUST]:
                    mixed_flavor = mix(board[leader_r][leader_c][FLAVOR], board[next_r][next_c][FLAVOR], 'strong')
                    attack_power -= (board[next_r][next_c][TRUST] + 1)
                    board[next_r][next_c][TRUST] += 1
                else:
                    mixed_flavor = mix(board[leader_r][leader_c][FLAVOR], board[next_r][next_c][FLAVOR], 'weak')
                    board[next_r][next_c][TRUST] += attack_power
                    attack_power = 0
                attacked.add((next_r, next_c))
                board[next_r][next_c][FLAVOR] = mixed_flavor
                next_r, next_c = next_r + dr[dir], next_c + dc[dir]

        count_flavor = {key: 0 for key in keys}
        for row in board:
            for col in row:
                count_flavor[col[0]] += col[1]

        for value in count_flavor.values():
            print(value, end=' ')
        print()

if __name__ == "__main__":
    main()

