import sys
input = sys.stdin.readline

n, m = map(int, input().split())

times = []
for _ in range(n):
    times.append(int(input()))
    
def check(mid):
    global times, m
    count = 0
    for i in times:
        count += mid // i
    return count < m

def binary_search():
    lo, hi = 0, 1000000000000000001
    
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        
        if check(mid):
            lo = mid
        else:
            hi = mid
    
    return hi
print(binary_search())
