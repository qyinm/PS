n = int(input())
stairs = []
for _ in range(n):
    stairs.append(int(input()))

dp = [0 for _ in range(n)]

def sol(n):
    dp[0] = stairs[0]
    if n == 1:
        return
    
    dp[1] = stairs[0] + stairs[1]
    if n == 2:
        return
    
    dp[2] = max(stairs[2] + stairs[0], stairs[2] + stairs[1])
    for i in range(3, n):
        dp[i] = stairs[i] + max(stairs[i-1] + dp[i-3], dp[i-2])
sol(n)
print(dp[-1])