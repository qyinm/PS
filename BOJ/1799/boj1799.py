n = int(input())
m = 0
MAX_N = 52
chess = []
adj = [[] for _ in range(MAX_N)]
aMatch = []
bMatch = []
visited = [0 for _ in range(MAX_N)]
left = [[0] * MAX_N for _ in range(MAX_N)]
right = [[0] * MAX_N for _ in range(MAX_N)]
visitCnt = 0



def fillLeft():
    y = 1
    x = n
    id = 1
    
    for k in range(0, 2*n-1):
        tmpy = y
        tmpx = x
        
        while tmpy <= n:
            left[tmpy][tmpx] = id
            tmpx += 1
            tmpy += 1
        id += 1
        x -= 1

def fillRight():
    y = n
    x = n
    id = 1
    
    for k in range(2*n-1):
        tmpy = y
        tmpx = x
        
        while tmpy > 0:
            right[tmpy][tmpx] = id
            tmpy -= 1
            tmpx += 1
        id += 1
        x -= 1

def biMatch():
    aMatch = [-1 for _ in range(n+1)]
    bMatch = [-1 for _ in range(m+1)]
    global visitCnt
    ans = 0
    
    for i in range(n):
        visitCnt += 1
        ans += dfs(i)

def dfs(idx):
    if visited[idx] == visitCnt:    return False
    visited[idx] = visitCnt
    
    for nx in range(len(adj[idx])):
        b = adj[idx][nx]
        if bMatch[b] == -1 or dfs(bMatch[b]):
            aMatch[idx] = b
            bMatch[b] = idx
            return True
        
    return False

for _ in range(n):
    chess.append(list(map(int, input().split())))

fillLeft()
fillRight()

maxL, maxR = 0, 0

for i in range(n):
    for j in range(n):
        if chess[i][j]:
            adj[left[i][j]].append(right[i][j])
            maxL = max(maxL, left[i][j])
            maxR = max(maxR, right[i][j])
n = maxL
m = maxR

print(biMatch())