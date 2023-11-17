n = int(input())

lo, hi = 0, n//2+1

while lo + 1 < hi:
    mid = (lo + hi) // 2
    
    if mid ** 2 <= n:
        lo = mid
    else:
        hi = mid
print(lo)
