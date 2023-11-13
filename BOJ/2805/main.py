import sys
input = sys.stdin.readline

n, m = map(int, input().split())

data = list(map(int, input().split()))
data.sort()

maxx = data[-1]

left, right = 0, maxx

def check(low):
    global data, m
    summ = 0
    for i in data:
        if i > low:
            summ += i - low
    return summ >= m

while left + 1 < right:
    mid = (left + right) // 2
    if check(mid):
        left = mid
    else:
        right = mid


print(left)
