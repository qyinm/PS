import sys
sys.setrecursionlimit(10**6)

MOD = 1_000_000_000

input = sys.stdin.readline

nums = [1] * 21
for i in range(1, 21):
    nums[i] = 2*nums[i-1]

def dp(cache, n, idx):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if cache[idx][n] != -1:
        return cache[idx][n]
    cache[idx][n] = 0
    for nxt in range(idx, -1, -1):
        cache[idx][n] += dp(cache, n - nums[nxt], nxt) % MOD
    return cache[idx][n] % MOD

def main():
    n = int(input())
    cache = [[-1] * (n+1) for _ in range(22)]
    start = 1
    while True:
        if 2**start > n:
            start -= 1
            break
        start += 1
        
    ans = dp(cache, n, start) % MOD
    print(ans)

if __name__ == "__main__":
    main()
