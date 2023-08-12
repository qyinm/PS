import sys

sys.setrecursionlimit(10**6)

tc: int
n: int
graph: list[int]
visited: list[int]
finished: list[bool]
cycle: int
id: int


def dfs(idx):
    global cycle, visited, finished, id
    visited[idx] = id
    id += 1
    if visited[graph[idx]] == -1:
        dfs(graph[idx])
    elif not finished[graph[idx]]:
        cycle += visited[idx] - visited[graph[idx]] + 1
    finished[idx] = True


def solve():
    global n, graph, cycle, visited, finished, id

    n = int(input())
    graph = [0 for _ in range(n + 1)]
    visited = [-1 for _ in range(n + 1)]
    finished = [False for _ in range(n + 1)]

    tmp = list(map(int, input().split()))

    for i in range(1, n + 1):
        graph[i] = tmp[i - 1]
    cycle = 0
    id = 0

    for i in range(1, n + 1):
        if not finished[i]:
            dfs(i)
    print(n - cycle)


tc = int(input())
for _ in range(tc):
    solve()
