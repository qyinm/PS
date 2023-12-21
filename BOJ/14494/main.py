dx = [1, 0, 1]
dy = [0, 1, 1]
MOD = 1e9 + 7
def main():
    n, m = map(int, input().split())
    cache = [[0] * (m) for _ in range(n)]
    cache[0][0] = 1
    for i in range(0, n):
        for j in range(0, m):
            for k in range(3):
                ny, nx = i + dy[k], j + dx[k]
                if ny < 0 or ny >= n or nx < 0 or nx >= m:
                    continue
                cache[ny][nx] += cache[i][j] % MOD
    
    print(int(cache[n-1][m-1] % MOD))
    
if __name__ == "__main__":
    main()
