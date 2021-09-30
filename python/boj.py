dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
idx = 0
mov = []
n = int(input())

game = [[0 for i in range(n+2)] for i in range(n+2)]
k = int(input())
for i in range(k):
    x, y = map(int, input().split())
    game[x][y] = '*'

l = int(input())
for i in range(l):
    c, key = input().split()
    c = int(c)
    temp = [c, key]
    mov.append(temp)
cycle = mov[-1][0]
for i in range(l-1, 0, -1):
    mov[i][0] -= mov[i-1][0]
time = 0
x = y = 1
movIdx = 0
game[1][1] = '-'
for i in range(cycle):
    if y < 1 or x < 1 or y > n or x > n :
        break
    next = game[y+dy[idx]][x+dx[idx]]
    if next == '*':
        game[y][x] = '-'
    elif next == '-':
        break
    else:
        game[y][x] = 0
    game[y+dy[idx]][x+dx[idx]] = '-'
    y += dy[idx]
    x += dx[idx]
    mov[movIdx][0] -= 1
    time += 1
    if mov[movIdx][0] == 0:
        if mov[movIdx][1] == 'D':
            idx += 1
        if mov[movIdx][1] == 'L':
            idx -= 1
        if idx > 3:
            idx = 0
        if idx < 0:
            idx = 3
        movIdx+=1
print(time)