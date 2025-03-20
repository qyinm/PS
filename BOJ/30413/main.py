import sys
input = sys.stdin.readline

MOD = 1_000_000_007

def calculate(n, m):
    if m == 0:
        return 1
    if m % 2 == 1:
        return (n % MOD) * (calculate(n, m - 1) % MOD)
    ret = calculate(n, m // 2) % MOD
    return (ret * ret) % MOD


def main():
    A, B = map(int, input().split())
    if A == 1:
        print(B % MOD)
        return
    upside = (calculate(A, B) - 1) % MOD
    mod_inverse = calculate(A - 1, MOD - 2) % MOD
    ans = (upside * mod_inverse) % MOD
    print(ans)

if __name__ == "__main__":
    main()