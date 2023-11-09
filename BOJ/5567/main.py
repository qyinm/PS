n = int(input())
m = int(input())
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
vis = [0 for _ in range(n+1)]

def dfs(dp, idx):
    global vis
    
    if vis[idx] == 1:
        ans = 0
    else:
        ans = 1
    vis[idx] = 1
    for i in range(2, n+1):
        if vis[i] != 0 or dp[idx][i] == 0:
            continue
        vis[i] = 1
        ans += vis[i]
    return ans

for _ in range(m):
    a, b = map(int, input().split())
    dp[a][b] = 1
    dp[b][a] = 1
    
ans = 0
for i in range(2, n+1):
    if dp[1][i] == 0:
        continue
    
    ans += dfs(dp, i)
print(ans)
