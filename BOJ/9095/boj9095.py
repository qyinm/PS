n = int(input())

dp = [0, 1, 2, 4]

for x in range(4, 12):
    dp.append(dp[x - 1] + dp[x - 2] + dp[x - 3])

for i in range(n):
    t = int(input())
    print(dp[t])
