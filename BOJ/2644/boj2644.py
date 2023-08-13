from typing import List

n = int(input())
start, end = map(int, input().split())
edge = int(input())

family = [[0 for i in range(n + 1)] for j in range(n + 1)]
visited: List[int] = [0 for _ in range(n + 1)]

for _ in range(edge):
    a, b = map(int, input().split())
    family[a][b] = 1
    family[b][a] = 1


# dfs
def dfs(start: int, find: int, cnt: int) -> None:
    if start == find:
        print(cnt)
        exit(0)
    for idx, el in enumerate(family[start]):
        if el == 0 or visited[idx] == 1:
            continue
        visited[idx] = 1
        dfs(idx, find, cnt + 1)


dfs(start, end, 0)
print(-1)
