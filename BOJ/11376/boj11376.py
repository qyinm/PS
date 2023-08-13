empolyer = []
visited = []
task = []
n, m = 0, 0

def dfs(start):
    global empolyer, visited, task
    
    for t in empolyer[start]:
        if visited[t]:  continue
        visited[t] = True
        if task[t] == 0 or dfs(task[t]):
            task[t] = start
            return True
    return False

def solution():
    global n, m, empolyer, visited, task
    ans = 0
    n, m = map(int, input().split())
    empolyer = [[] for _ in range(1001)]
    task = [0 for _ in range(1001)]
    for i in range(1, n+1):
        empolyer[i] = list(map(int, input().split()))[1:]
    for i in range(1,n+1):
        for _ in range(2):
            visited = [False for _ in range(1001)]
            if dfs(i):
                ans += 1
    print(ans) 

solution()