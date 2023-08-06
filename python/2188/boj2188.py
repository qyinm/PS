import sys

employee = [[] for _ in range(1001)]
task = [0 for _ in range(1001)]
visited = []

def dfs(start):
    global visited, task, employee
    if visited[start]:  return False
    visited[start] = True
    for t in employee[start]:
        if task[t] == 0 or dfs(task[t]):
            task[t] = start
            return True
    return False

def solution():
    global visited, employee
    n, m = map(int, input().split())
    for i in range(1, n+1):
        employee[i] = list(map(int, sys.stdin.readline().rstrip().split()))[1:]
    cnt = 0
    for i in range(1, n+1):
        visited = [False for _ in range(1001)]
        if dfs(i): cnt+=1
    print(cnt)
solution()