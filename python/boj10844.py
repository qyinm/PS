n = int(input())

dp = [[0,1,1,1,1,1,1,1,1,1],[1,1,2,2,2,2,2,2,2,1]]
for x in range(1, n):
    tp = [0 for _ in range(10)]
    tp[0] = dp[x][1]
    for y in range(1, 9):
        tp[y] = dp[x][y-1] + dp[x][y+1]
    tp[9] = dp[x][8]
    dp.append(tp)
print(sum(dp[n-1])%1000000000)