dx =[]
dy =[]
for i in range(3):
    x, y = map(int, input().split())
    dx.append(x)
    dy.append(y)

for i in range(3):
    if dx.count(dx[i]) == 1:
        x = dx[i]
    if dy.count(dy[i]) == 1:
        y = dy[i]

print(x, y)