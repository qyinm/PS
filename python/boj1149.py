n = int(input())

cost = [[0 for _ in range(3)] for x in range(n+1)]

for i in range(1, n+1):
    r, g, b = map(int, input().split())
    cost[i][0] += min(cost[i-1][1], cost[i-1][2]) + r
    cost[i][1] += min(cost[i-1][0], cost[i-1][2]) + g
    cost[i][2] += min(cost[i-1][0], cost[i-1][1]) + b

print(min(cost[n]))