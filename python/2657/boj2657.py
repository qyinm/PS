import sys

t = int(input())

for _ in range(t):
    r, string = input().split()
    r = int(r)
    for s in string:
        print(s*r, end="")
    print()