import sys

input = sys.stdin.readline


def can_pass(line: list[int], l: int) -> bool:
    n = len(line)
    j = 0
    prev_dir = None
    while j < n:
        tmp_idx = next((k for k in range(j + 1, n) if line[j] != line[k]), n)
        if tmp_idx == n:
            return True
        next_idx = next((k for k in range(tmp_idx + 1, n) if line[tmp_idx] != line[k]), n)
        diff = line[tmp_idx] - line[j]

        if diff == 1 and (j + 2 * l if prev_dir == "down" else j + l) <= tmp_idx:
            prev_dir = "up"
        elif diff == -1 and tmp_idx + l <= next_idx:
            prev_dir = "down"
        else:
            return False
        j = tmp_idx
    return True


def main():
    n, l = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    rows = (board[i] for i in range(n))
    cols = ([board[j][i] for j in range(n)] for i in range(n))
    print(sum(can_pass(line, l) for line in (*rows, *cols)))


if __name__ == "__main__":
    main()
