import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split(' '))
graph = [[] for _ in range(N+1)]

for _ in range(M):
    person, com = map(int, input().rstrip().split(' '))
    graph[person].append(com)

visited = [False for _ in range(N+1)]
matched = [-1 for _ in range(N+1)]
def bimatch(curr):
    global visited, graph, matched
    if visited[curr] == True:
        return False
    visited[curr] = True
    
    for com in graph[curr]:
        if matched[com] == -1 or bimatch(matched[com]):
            matched[com] = curr
            return True
    
    return False
    
ans = 0
for i in range(1, N+1):
    visited = [False for _ in range(N+1)]
    if bimatch(i):
        ans += 1
        
print(ans)