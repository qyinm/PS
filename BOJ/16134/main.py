import sys
input = sys.stdin.readline

MOD = 1_000_000_007

def power(base, exp):
    if exp == 0:
        return 1
    if exp % 2 == 1:
        return (base * power(base, exp - 1)) % MOD
    half = power(base, exp // 2)
    return (half * half) % MOD

# 팩토리얼 계산 (모듈러 적용)
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = (result * i) % MOD
    return result

def main():
    n, m = map(int, input().split())
    
    a = factorial(n)
    b = factorial(m)
    c = factorial(n - m)
    
    bc = (b * c) % MOD
    bc = power(bc, MOD - 2)
    
    ans = (a * bc) % MOD
    print(ans)

if __name__ == "__main__":
    main()