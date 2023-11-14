import sys
input = sys.stdin.readline

n, m = map(int, input().split())

v = []
for _ in range(m):
    v.append(int(input()))
v.sort()

def check(mid):
    global v, n
    
    count = 0
    for i in v:
        count += i // mid
        if i % mid != 0:
            count += 1
    return count > n

def binary_search():
    global v
    
    lo, hi = 0, v[-1] + 1
    
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        
        if check(mid):
            lo = mid
        else:
            hi = mid
    print(hi)
binary_search()
    
