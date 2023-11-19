import sys
input = sys.stdin.readline

tc = int(input())

def binary_search(av, b):
    
    lo, hi = -1, len(b)
    
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if av > b[mid]:
            lo = mid
        else:
            hi = mid
    return lo + 1 

for _ in range(tc):
    n, m = map(int, input().split())
    a = [*map(int, input().split())]
    b = [*map(int, input().split())]
    
    b.sort()
    cnt = 0
    for av in a:
        cnt += binary_search(av, b)
    print(cnt)
