import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

MOD = 1_000_000_007

def getPow(n, exp):
    if exp == 1:
        return n
    if exp % 2 == 1:
        return ((n % MOD) * (getPow(n, exp - 1) % MOD)) % MOD
    ret = getPow(n, exp // 2) % MOD
    return (ret * ret) % MOD

def main():
    M = int(input())
    ans = 0

    for _ in range(M):
        N, S = map(int, input().split())
        ans = ((ans % MOD) + (((S % MOD) * (getPow(N, MOD-2) % MOD)) % MOD)) % MOD
    print(ans)

if __name__ == "__main__":
    main()