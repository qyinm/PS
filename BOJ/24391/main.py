import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [i for i in range(n+1)]

def getParent(x):
    global graph
    if graph[x] == x:
        return x
    graph[x] = getParent(graph[x])
    return graph[x]

def find(a, b):
    a = getParent(a)
    b = getParent(b)
    
    return a != b

def union(a, b):
    global graph
    a = getParent(a)
    b = getParent(b)
    if a < b:
        graph[b] = a
    else:
        graph[a] = b

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)
    
classes = [*map(int, input().split())]



prev = classes[0]

ans = 0
for i in range(1, n):
    if find(prev, classes[i]):
        ans += 1
    prev = classes[i]
print(ans)
    
