import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

def move(r, c, cmd):
    match cmd:
        case 'R':
            c += 1
        case 'L':
            c -= 1
        case 'U':
            r -= 1
        case 'D':
            r += 1
    return [r, c]

def dfs(r, c, n, m, graph, cache):
    if r >= n or r < 0 or c >= m or c < 0:
        return 1
    if cache[r][c] != -1:
        return cache[r][c]
    nr, nc = move(r, c, graph[r][c])
    cache[r][c] = 0
    cache[r][c] = dfs(nr, nc, n, m, graph, cache)
    return cache[r][c]

def main():
    n, m = map(int, input().split())
    graph = [[*input().rstrip()] for _ in range(n)]
    cache = [[-1] * m for _ in range(n)]
    
    for r in range(n):
        for c in range(m):
            if cache[r][c] != -1:
                continue
            dfs(r, c, n, m, graph, cache)
    ans = 0
    for ca in cache:
        for c in ca:
            if c == 1:
                ans += 1
    print(ans)
if __name__ == "__main__":
    main()
