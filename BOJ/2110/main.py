import sys
input = sys.stdin.readline

n, c = map(int, input().split())

v = []

for _ in range(n):
    v.append(int(input()))
v.sort()

def check(mid):
    global v, c
    current = v[0]
    count = 1
    for i in range(1, n):
        if current + mid <= v[i]:
            current = v[i]
            count += 1
    # print(f'mid {mid} count {count}') 
    return count >= c

def binary_search():
    global v, n, c
    lo, hi = 0, v[-1]+1
    
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if check(mid):
            lo = mid
        else:
            hi = mid
    print(lo)

binary_search()
