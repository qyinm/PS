import sys
input = sys.stdin.readline

n = int(input())


def binary_search():
    global n
    lo, hi = -1, 2**32
    
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid**2 < n :
            lo = mid
        else:
            hi = mid
    print(hi)

binary_search()
