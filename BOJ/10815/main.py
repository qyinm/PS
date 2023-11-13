import sys
input = sys.stdin.readline

n = int(input())

data = list(map(int, input().split()))
data.sort()

m = int(input())
finds = list(map(int, input().split()))

def bs(find):
    global data, n
    lo, hi = -1, n
    
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if data[mid] < find:
            lo = mid
        else:
            hi = mid
    return hi < n and data[hi] == find


for find in finds:
    if bs(find):
        print(1, end = ' ')
    else:
        print(0, end = ' ')


