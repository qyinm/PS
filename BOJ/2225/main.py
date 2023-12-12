import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
MOD = 1_000_000_000
def dp(n, k, cache):
    if k < 0 or n < 0:
        return 0
    if n == 0 and k == 0:
        return 1
    
    if cache[n][k] != -1:
        return cache[n][k] % MOD

    cache[n][k] = 0
    
    for i in range(n + 1):
        cache[n][k] += dp(n - i, k - 1, cache)
    
    return cache[n][k] % MOD

def main():
    n, k = map(int, input().split())
    cache = [[-1 for _ in range(k + 1)] for _ in range(n + 1)]
    
    ans = dp(n, k, cache) % MOD
    print(ans)
    
if __name__ == "__main__":
    main()
