import sys
sys.setrecursionlimit(int(1e6))

input = sys.stdin.readline

def dp(a, b, memo, i, j):
    if i == len(a) or j == len(b):
        return 0
    
    if memo[i][j] != -1:
        return memo[i][j]
    
    if a[i] == b[j]:
        memo[i][j] = 1 + dp(a, b, memo, i + 1, j + 1)
    else:
        memo[i][j] = max(dp(a, b, memo, i + 1, j), dp(a, b, memo, i, j + 1))
    
    return memo[i][j]

def main():
    a = input().rstrip()
    b = input().rstrip()

    memo = [[-1] * len(b) for _ in range(len(a))]

    dp(a, b, memo, 0, 0)

    # 문자열 추적
    i, j = 0, 0
    lcs = []
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            lcs.append(a[i])
            i += 1
            j += 1
        elif i + 1 < len(a) and memo[i + 1][j] >= (memo[i][j + 1] if j + 1 < len(b) else 0):
            i += 1
        else:
            j += 1

    print(len(lcs))
    print(''.join(lcs))

if __name__ == "__main__":
    main()