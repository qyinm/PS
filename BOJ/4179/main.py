import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())

miro = [[*input().rstrip()] for _ in range(r)]
visited = [[False for _ in range(c)] for _ in range(r)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

fireq = deque([])
jq = deque([])

for row in range(r):
    for col in range(c):
        if miro[row][col] == 'J':
            jq.append([row, col, 1])
        elif miro[row][col] == 'F':
            fireq.append([row, col])
            
def bfs(jq, fireq):
    addjq = deque([])
    addfq = deque([])
    while jq:
        while jq:
            [jrow, jcol, time] = jq.popleft()
            if miro[jrow][jcol] == 'F':
                continue
            if jrow == 0 or jcol == 0 or jrow == r-1 or jcol == c-1:
                print(time)
                exit(0)
                break
            for i in range(4):
                njrow, njcol = jrow + dy[i], jcol + dx[i]
                if njrow < 0 or njrow >= r or njcol < 0 or njcol >= c:
                    continue
                if miro[njrow][njcol] == 'F' or miro[njrow][njcol] == '#':
                    continue
                if visited[njrow][njcol]:
                    continue
                visited[njrow][njcol] = True
                addjq.append([njrow, njcol, time + 1])
        while addjq:
            jq.append(addjq.popleft())
            
        while fireq:
            [frow, fcol] = fireq.popleft()
            for i in range(4):
                nfrow, nfcol = frow + dy[i], fcol + dx[i]
                if nfrow < 0 or nfrow >= r or nfcol < 0 or nfcol >= c:
                    continue
                if miro[nfrow][nfcol] == '#' or miro[nfrow][nfcol] == 'F':
                    continue
                addfq.append([nfrow, nfcol])
                miro[nfrow][nfcol] = 'F'
        while addfq:
            fireq.append(addfq.popleft())
    print("IMPOSSIBLE")
        
bfs(jq, fireq)
    
