import sys
input = sys.stdin.readline

n = int(input())
plist = [0] + list(map(int, input().rstrip().split(' ')))
cache = [0 for _ in range(1001)]


def dp(cnt):
    global cache
    if cnt == 0:
        return 0
    
    if cache[cnt] != 0:
        return cache[cnt]
    
    
    for i in range(cnt):
        cache[cnt] = max(dp(cnt - (i + 1)) + plist[i+1], cache[cnt])
    return cache[cnt]

print(dp(n))
