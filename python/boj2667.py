n = int(input())

t = 0

def dfs(x, y):
    if x<= -1 or x>=n or y<= -1 or y>=n:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0

        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        global t
        t += 1
        return True
    return False    

graph=[]
result = []
for x in range(n):
    graph.append(list(map(int,input())))
for i in range(n):
    for j in range(n):
        t = 0
        if dfs(i, j) == True:
            result.append(t)
print(len(result))
result.sort()
for i in result:
    print(i)