import sys
input = sys.stdin.readline
n = int(input())
ans = 0
s = set()
for _ in range(n):
    in_data = input().strip()
    if in_data == "ENTER":
        ans += len(s)
        s = set()
        continue
    s.add(in_data)
print(ans + len(s))