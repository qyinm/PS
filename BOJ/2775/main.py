import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
t = int(input())
def recur(k, n):
    if k < 0 or n < 0:
        return 0
    if cache[k][n] != -1:
        return cache[k][n]
    
    cache[k][n] = recur(k, n - 1) + recur(k - 1, n)
    return cache[k][n]
for _ in range(t):
    k = int(input())
    n = int(input())
    cache = [[-1] * (n + 1) for _ in range(k + 1)]
    
    cache[0] = [i for i in range(n + 1)]

    ans = recur(k, n)
    print(ans)
