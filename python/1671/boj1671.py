sharks = []
bite = [-1 for _ in range(51)]
visited = [False for _ in range(51)]
n = 0

def check(a, b):
    global sharks
    if sharks[a][0] == sharks[b][0] and sharks[a][1] == sharks[b][1] and sharks[a][2] == sharks[b][2] and a < b:
        return False
    if sharks[a][0] >= sharks[b][0] and sharks[a][1] >= sharks[b][1] and sharks[a][2] >= sharks[b][2]:
        return True
    return False

def dfs(x):
    global sharks, bite, n
    if visited[x]:  return False
    visited[x] = True
    for i in range(n):
        if i == x:  continue
        if not check(x, i):    continue
        if bite[i] == -1 or dfs(bite[i]):
            bite[i] = x
            return True
    return False

def solution():
    global n, sharks, visited
    n = int(input())
    for _ in range(n):
        sharks.append(list(map(int, input().split())))

    cnt = 0
    for i in range(n):
        for _ in range(2):
            visited = [False for _ in range(51)]
            if dfs(i):  cnt += 1
    
    print(n-cnt)

solution()