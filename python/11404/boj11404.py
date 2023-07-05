import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

cost = [[INF]*(n+1) for _ in range(n + 1)]
for i in range(1, n + 1):
    cost[i][i] = 0
    
for i in range(m):
    s, e, c = map(int, input().split())
    cost[s][e] = min(c, cost[s][e])
for k in range(1, n + 1):
    for start in range(1, n + 1):
        for end in range(1, n + 1):
            cost[start][end] = min(cost[start][end], cost[start][k] + cost[k][end])

for i in range(1, n+1):
    for j in range(1, n+1):
        if cost[i][j] == INF:
            print(0, end=" ")
        else:
            print (cost[i][j], end=" ")
    print()