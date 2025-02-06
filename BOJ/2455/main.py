import sys
input = sys.stdin.readline

maxx = 0
now = 0
for _ in range(4):
    a, b = map(int, input().split())
    now = b - a + now
    maxx = max(maxx, now)
print(maxx)