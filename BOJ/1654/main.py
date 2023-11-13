import sys
input = sys.stdin.readline

n, m = map(int, input().split())

data = []
for _ in range(n):
    data.append(int(input().rstrip()))
data.sort()

maxx = data[-1]

left, right = 1, maxx+1

def check(low):
    global data, m
    summ = 0
    for i in data:
        summ += i // low
    return summ >= m

while left + 1 < right:
    mid = (left + right) // 2
    if check(mid):
        left = mid
    else:
        right = mid
print(left)
