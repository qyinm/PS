import sys
sys.setrecursionlimit(10**6)

cards = []
cache = []
n = 0

def dp(lidx, ridx):
    global n, cards, cache
    if cache[lidx][ridx] != -1:
        return cache[lidx][ridx]
    if lidx == n or ridx == n:
        return 0
    cache[lidx][ridx] = 0
    if cards[0][lidx] > cards[1][ridx]:
        cache[lidx][ridx] = cards[1][ridx] + dp(lidx, ridx+1) 
    else:
        allInc = dp(lidx+1, ridx+1)
        leftInc = dp(lidx+1, ridx)
        cache[lidx][ridx] = max(allInc, leftInc)
    return cache[lidx][ridx]


def solution():
    global n, cards, cache
    n = int(input())
    
    for _ in range(2):
        cards.append(list(map(int, input().split())))
    cache = [[-1] * (n+1) for _ in range(n+1)]
    print(dp(0, 0))

solution()