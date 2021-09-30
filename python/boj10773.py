import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    tmp = int(input())
    if tmp:
        stack.append(tmp)
    else:
        stack.pop()
print(sum(stack))