import sys
sys.setrecursionlimit(10**6)

MOD = 1_000_000_007
cache = []
def dp(n, num, val):
    if n == 0:
        return val % 15 == 0
    if cache[n][num] != -1:
        return cache[n][num]
    cache[n][num] = dp(n-1, num+1, val+1*(10**(n-1)))%MOD + dp(n-1, num+5, val+5*(10**(n-1)))%MOD
    #print(cache[num][n])
    return cache[n][num]%MOD

def main():
    global cache
    n = int(input())
    cache = [[-1] * (8000) for _ in range(n+1)]
    if n < 3:
        print(n-1)
        return
    ans = dp(n, 0, 0)
    print(ans)
    
main()
