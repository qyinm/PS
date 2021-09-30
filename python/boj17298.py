import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
nge = [-1] * n
stack = [0]
i = 1
while stack and i < n:
    while stack and data[stack[-1]] < data[i]:
        nge[stack[-1]] = data[i]
        stack.pop()
    stack.append(i)
    i += 1

print(' '.join(map(str, nge)))