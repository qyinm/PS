import sys
input = sys.stdin.readline

n = int(input())

v = [*map(int, input().split())]
maxx = int(input())
v.sort()

def check(mid):
    global v, maxx
    
    summ = 0
    for i in v:
        if mid < i:
            summ += mid
        else:
            summ += i
    return summ <= maxx 

def binary_search():
    global v, maxx
    lo, hi = -1, v[-1] + 1
    
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if check(mid):
            lo = mid
        else:
            hi = mid
    print(lo)

binary_search()
