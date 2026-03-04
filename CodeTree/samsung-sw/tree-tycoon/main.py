from collections import deque

DIRS = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]
GROW_DIRS = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

def main():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    command = []
    for _ in range(m):
        d, p = map(int, input().split())
        command.append((d - 1, p))

    boosters = deque([(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)])
    for (d, p) in command:
        dr, dc = DIRS[d]
        
        boost_len = len(boosters)
        for _ in range(boost_len):
            br, bc = boosters.popleft()
            nbr = (dr * p + br) % n
            nbc = (dc * p + bc) % n

            boosters.append((nbr, nbc))
        
        for (br, bc) in boosters:
            board[br][bc] += 1
        
        growup_trees = []
        while boosters:
            (br, bc) = boosters.popleft()
            cnt = 0
            for dr, dc in GROW_DIRS:
                nbr = (br + dr)
                nbc = (bc + dc)
                if not (0 <= nbr < n and 0 <= nbc < n):
                    continue

                if board[nbr][nbc] > 0:
                    cnt += 1
            growup_trees.append((cnt, br, bc))

        visited = set()
        for cnt, br, bc in growup_trees:
            if cnt == 0:
                continue
            board[br][bc] += cnt
            visited.add((br, bc))
        
        for r in range(n):
            for c in range(n):
                if (r, c) in visited or board[r][c] < 2:
                    continue
                
                board[r][c] -= 2
                boosters.append((r, c))
    print(sum([sum(row) for row in board]))

if __name__ == "__main__":
    main()